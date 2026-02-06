# Security Pitfalls

## TL;DR

- Erreurs classiques : `sudo()` partout, droits trop larges, règles contradictoires.
- Toujours tester avec des comptes non-admin.

## Checklist

- [ ] Vérifier ACL minimales.
- [ ] Vérifier règles par company/owner.
- [ ] Réduire/justifier chaque `sudo()`.
- [ ] Valider que les endpoints controller respectent `auth` + droits.
