# Structure (Data Files)

> Doc officielle : https://www.odoo.com/documentation/19.0/developer/reference/backend/data.html

## TL;DR

- Les data files définissent des données via XML (et parfois CSV).
- Les opérations sont exécutées séquentiellement : on ne peut référencer que ce qui a été créé avant.

## Concepts clés

- Racine `<odoo>` et opérations `<record>`, `<menuitem>`, `<template>`, `<function>`, etc.
- Gestion d’identifiants : `id` + `module` → `xmlid` stocké dans `ir.model.data`.
- `noupdate="1"` : data initiale protégée des updates (avec nuances).

## Patterns recommandés

- Séparer `data/` (config) et `demo/` (données démo).
- Toujours prefixer les ids de manière claire (ex: `view_x_form`, `action_x`).
- Garder les fichiers petits et thématiques (views, security, actions…).

## Pièges fréquents

- Référencer un xmlid non encore chargé (ordre des fichiers dans manifest).
- Mettre tout en `noupdate=1` puis vouloir mettre à jour plus tard (difficile).

## Checklist

- [ ] Déclarer les fichiers dans `__manifest__.py` (`data`, `demo`).
- [ ] Vérifier l’ordre de chargement.
- [ ] Tester upgrade de module (mise à jour).

## Exemples

```xml
<?xml version="1.0" encoding="UTF-8"?>
<odoo>
  <record id="x_tag_demo" model="x.tag">
    <field name="name">Demo</field>
  </record>
</odoo>
```
