# Reference List (Generic Components)

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/owl_components.html#reference-list

## TL;DR
Le framework fournit une suite de composants génériques réutilisables.

| Composant | Description | Import |
| :--- | :--- | :--- |
| **ActionSwiper** | Actions par glissement (swipe) horizontal. | `@web/core/action_swiper/action_swiper` |
| **CheckBox** | Case à cocher simple avec label. | `@web/core/checkbox/checkbox` |
| **ColorList** | Liste de sélection de couleurs. | `@web/core/colorlist/colorlist` |
| **Dropdown** | Menu déroulant complet. | `@web/core/dropdown/dropdown` |
| **Notebook** | Interface à onglets. | `@web/core/notebook/notebook` |
| **Pager** | Pagination (ex: 9-12 / 20). | `@web/core/pager/pager` |
| **SelectMenu** | Select avancé (recherche, groupes). | `@web/core/select_menu/select_menu` |
| **TagsList** | Liste de tags (badges arrondis). | `@web/core/tags_list/tags_list` |

---

## Détails des Composants

### ActionSwiper
Enveloppe un élément pour lui ajouter des actions au swipe (gauche/droite).
Très utile pour les listes sur mobile (ex: Archiver, Supprimer).

```xml
<ActionSwiper onRightSwipe="{ action: deleteItem, icon: 'fa-delete', bgColor: 'bg-danger' }">
    <div>Item</div>
</ActionSwiper>
```

### CheckBox
Case à cocher liée à son label.

```xml
<CheckBox value="state.isChecked" t-on-change="onCheck" disabled="false">
    Activer l'option
</CheckBox>
```

### Dropdown
Nécessite deux slots : `default` (le déclencheur/bouton) et `content` (le menu).
Supporte les `DropdownItem`.

```xml
<Dropdown>
    <button>Menu</button>
    <t t-set-slot="content">
        <DropdownItem onSelected="doAction">Action 1</DropdownItem>
    </t>
</Dropdown>
```

### Notebook
Onglets horizontaux ou verticaux. Pages définies via slots ou props.

```xml
<Notebook>
    <t t-set-slot="page_1" title="'Général'">
        <Content1/>
    </t>
    <t t-set-slot="page_2" title="'Options'">
        <Content2/>
    </t>
</Notebook>
```

### Pager
Affiche "offset-limit / total".
**Props :** `offset`, `limit`, `total`, `onUpdate`.

```xml
<Pager offset="0" limit="80" total="100" onUpdate="updatePager"/>
```

### SelectMenu
Alternative puissante au `<select>` natif.
Supporte la recherche (`searchable`), la multi-sélection (`multiSelect`), les groupes.

```javascript
const choices = [
    { value: 'a', label: 'Choix A' },
    { value: 'b', label: 'Choix B' }
];
```
```xml
<SelectMenu choices="choices" value="'a'" onSelect="selectKey"/>
```
