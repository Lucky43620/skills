"""Audit the coverage matrix without external dependencies.

This script reads the XLSX file using the OpenXML structure (zip + XML) to
avoid relying on openpyxl when it cannot be installed in the environment.
"""

from __future__ import annotations

import csv
import re
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import xml.etree.ElementTree as ET


NS = {"main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
REQUIRED_SECTIONS = [
    "TL;DR",
    "Quand l’utiliser",
    "Concepts clés",
    "API / Syntaxe",
    "Patterns recommandés",
    "Anti-patterns & pièges",
    "Debug & troubleshooting",
    "Exemples complets",
    "Checklist",
    "Liens officiels",
    "Voir aussi",
]


@dataclass
class Sheet:
    name: str
    target: str


def col_to_index(col: str) -> int:
    idx = 0
    for ch in col:
        idx = idx * 26 + (ord(ch) - 64)
    return idx


def iter_sheets(zf: zipfile.ZipFile) -> list[Sheet]:
    wb = ET.fromstring(zf.read("xl/workbook.xml"))
    sheets: list[Sheet] = []
    for sheet in wb.find("main:sheets", NS):
        name = sheet.attrib["name"]
        rid = sheet.attrib[
            "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
        ]
        sheets.append(Sheet(name=name, target=rid))

    rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    relmap = {rel.attrib["Id"]: rel.attrib["Target"] for rel in rels}
    for sheet in sheets:
        sheet.target = relmap[sheet.target]
    return sheets


def cell_value(cell: ET.Element) -> str | None:
    cell_type = cell.attrib.get("t")
    if cell_type == "inlineStr":
        inline = cell.find("main:is", NS)
        if inline is None:
            return None
        return "".join(t.text or "" for t in inline.findall(".//main:t", NS))
    value = cell.find("main:v", NS)
    if value is None:
        return None
    return value.text


def read_rows(
    zf: zipfile.ZipFile,
    target: str,
    max_rows: int | None = None,
    max_cols: int = 30,
) -> list[list[str | None]]:
    data = ET.fromstring(zf.read(target.lstrip("/")))
    rows: list[list[str | None]] = []
    for idx, row in enumerate(data.findall("main:sheetData/main:row", NS)):
        if max_rows is not None and idx >= max_rows:
            break
        values: list[str | None] = [None] * max_cols
        for cell in row.findall("main:c", NS):
            r = cell.attrib.get("r")
            if not r:
                continue
            col = "".join(ch for ch in r if ch.isalpha())
            col_idx = col_to_index(col) - 1
            if col_idx >= max_cols:
                continue
            values[col_idx] = cell_value(cell)
        rows.append(values)
    return rows


def detect_sheet_with_path_status(
    sheets: Iterable[Sheet],
    zf: zipfile.ZipFile,
) -> list[str]:
    matches: list[str] = []
    for sheet in sheets:
        rows = read_rows(zf, sheet.target, max_rows=10, max_cols=40)
        for row in rows:
            if row and "Path" in row and "Status" in row:
                matches.append(sheet.name)
                break
    return matches


def pick_work_queue(
    sheets: dict[str, Sheet],
    zf: zipfile.ZipFile,
) -> tuple[str | None, list[list[str | None]]]:
    for name in ("Work Queue", "All Pages", "Topic Summary"):
        sheet = sheets.get(name)
        if sheet is None:
            continue
        rows = read_rows(zf, sheet.target, max_rows=None, max_cols=40)
        if len(rows) < 2:
            continue
        header = rows[0]
        if "Path" in header and "Status" in header:
            return name, rows
        if name in {"All Pages", "Topic Summary"}:
            return name, rows
    return None, []


def write_preview_csv(rows: list[list[str | None]], path: Path, limit: int = 10) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        for row in rows[:limit]:
            writer.writerow([cell or "" for cell in row])


def extract_links(text: str) -> list[str]:
    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    return pattern.findall(text)


def scan_markdown_files(base_dir: Path) -> dict[str, dict[str, object]]:
    results: dict[str, dict[str, object]] = {}
    for path in base_dir.rglob("*.md"):
        rel_path = path.as_posix()
        content = path.read_text(encoding="utf-8")
        words = len(re.findall(r"\b\\w+\\b", content))
        headings = re.findall(r"^##\\s+(.+)$", content, flags=re.MULTILINE)
        missing_sections = [
            section for section in REQUIRED_SECTIONS if section not in headings
        ]
        short_without_sections = words < 120 and not headings
        broken_links: list[str] = []
        for link in extract_links(content):
            if link.startswith(("http://", "https://", "#", "mailto:")):
                continue
            if link.startswith("/"):
                target = base_dir.parent / link.lstrip("/")
            else:
                target = (path.parent / link).resolve()
            if target.suffix == ".md" and not target.exists():
                broken_links.append(link)
        results[rel_path] = {
            "words": words,
            "headings": headings,
            "missing_sections": missing_sections,
            "short_without_sections": short_without_sections,
            "broken_links": broken_links,
        }
    return results


def main() -> int:
    xlsx_path = Path("odoo_v19_skill_coverage_matrix.xlsx")
    if not xlsx_path.exists():
        print("XLSX introuvable.")
        return 1

    report_path = Path("coverage_report.md")

    markdown_scan = scan_markdown_files(Path("references"))

    status_counts: dict[str, int] = {}

    with zipfile.ZipFile(xlsx_path) as zf:
        sheets = iter_sheets(zf)
        sheet_map = {sheet.name: sheet for sheet in sheets}
        sheet_names = [sheet.name for sheet in sheets]

        preview_rows = {
            sheet.name: read_rows(zf, sheet.target, max_rows=10, max_cols=20)
            for sheet in sheets
        }

        matches = detect_sheet_with_path_status(sheets, zf)
        queue_name, queue_rows = pick_work_queue(sheet_map, zf)

        all_pages = sheet_map.get("All Pages")
        if all_pages:
            rows = read_rows(zf, all_pages.target, max_rows=None, max_cols=40)
            if rows:
                header = rows[0]
                if "Status" in header:
                    status_idx = header.index("Status")
                    for row in rows[1:]:
                        status = row[status_idx]
                        if status:
                            status_counts[status] = status_counts.get(status, 0) + 1

    with report_path.open("w", encoding="utf-8") as handle:
        handle.write("# Coverage report (audit XLSX)\n\n")
        handle.write(
            "Ce rapport est généré via un lecteur OpenXML minimal (pas de dépendance "
            "`openpyxl`).\n\n"
        )
        handle.write("## Onglets détectés\n\n")
        for name in sheet_names:
            handle.write(f"- {name}\n")

        if status_counts:
            total = sum(status_counts.values())
            handle.write("\n## Totaux par statut (All Pages)\n\n")
            handle.write(f"Total pages: **{total}**\n\n")
            for status in sorted(status_counts):
                handle.write(f"- {status}: {status_counts[status]}\n")

        handle.write("\n## Feuilles avec colonnes `Path` et `Status`\n\n")
        if matches:
            for name in matches:
                handle.write(f"- {name}\n")
        else:
            handle.write("- Aucun onglet avec `Path` + `Status` détecté.\n")

        handle.write("\n## Aperçu (10 premières lignes)\n\n")
        for name, rows in preview_rows.items():
            handle.write(f"### {name}\n\n")
            handle.write("```text\n")
            for row in rows:
                handle.write("|" + "|".join(cell or "" for cell in row) + "|\n")
            handle.write("```\n\n")

        handle.write("## File d'attente (work queue)\n\n")
        if queue_name is None:
            handle.write(
                "Aucune feuille exploitable détectée. Utiliser le scan des placeholders.\n"
            )
        else:
            handle.write(f"Source utilisée : **{queue_name}**\n\n")
            if len(queue_rows) < 2:
                handle.write("Feuille vide ou inutilisable.\n")
            else:
                header = queue_rows[0]
                status_idx = header.index("Status") if "Status" in header else None
                path_idx = header.index("Path") if "Path" in header else None
                priority_idx = (
                    header.index("PriorityHint") if "PriorityHint" in header else None
                )
                filtered = []
                for row in queue_rows[1:]:
                    if status_idx is None or path_idx is None:
                        continue
                    status = row[status_idx] or ""
                    if status in {"Placeholder", "Stub", "Draft"}:
                        filtered.append(row)
                handle.write(
                    f"Entrées à traiter (Placeholder/Stub/Draft): **{len(filtered)}**\n\n"
                )
                handle.write("|Statut|Priorité|Fichier|\n|---|---|---|\n")
                for row in filtered:
                    status = row[status_idx] or ""
                    path = row[path_idx] or ""
                    priority = row[priority_idx] if priority_idx is not None else ""
                    handle.write(f"|{status}|{priority}|{path}|\n")

        handle.write("\n## Audit markdown (sections / liens / longueur)\n\n")
        handle.write(
            "Ce tableau liste les pages avec sections manquantes, liens internes cassés "
            "ou contenu très court sans sections.\n\n"
        )
        handle.write(
            "|Fichier|Mots|Sections manquantes|Liens cassés|Court sans sections|\n"
            "|---|---|---|---|---|\n"
        )
        for rel_path, info in sorted(markdown_scan.items()):
            missing = ", ".join(info["missing_sections"]) or "—"
            broken = ", ".join(info["broken_links"]) or "—"
            short = "Oui" if info["short_without_sections"] else "Non"
            if missing != "—" or broken != "—" or short == "Oui":
                handle.write(
                    f"|{rel_path}|{info['words']}|{missing}|{broken}|{short}|\n"
                )

    preview_csv = Path("coverage_report_preview.csv")
    if queue_rows:
        write_preview_csv(queue_rows, preview_csv, limit=20)
    print(f"Report écrit: {report_path}")
    if preview_csv.exists():
        print(f"CSV aperçu: {preview_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
