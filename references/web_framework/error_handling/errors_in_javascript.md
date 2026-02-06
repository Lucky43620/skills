# Errors in JavaScript

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/error_handling.html

## TL;DR

- Distinguer erreurs attendues (validation) vs erreurs inattendues (bug).
- Préférer notifier l’utilisateur proprement plutôt que throw brut.

## Patterns recommandés

- Pour validation : retourner un feedback UI (notification/dialog) plutôt que throw.
- Logger les erreurs inattendues et rethrow si nécessaire.

## Pièges fréquents

- Throw pour du contrôle de flux (anti-pattern) → code difficile à maintenir.
