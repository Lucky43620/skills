# Best Practices (Owl)

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/owl_components.html#best-practices

## 1. Pas de `constructor`
Les composants Owl sont des classes, mais **vous ne devriez jamais utiliser le `constructor`**.
Utilisez la méthode `setup()` à la place.
Le `constructor` n'est pas surchargeable proprement dans le contexte des mixins/extensions Odoo.

**Incorrect :**
```javascript
class IncorrectComponent extends Component {
    constructor(parent, props) { // JAMAIS !
        super(...arguments);
        this.state = useState({});
    }
}
```

**Correct :**
```javascript
class MyComponent extends Component {
    setup() {
        this.state = useState({});
    }
}
```

## 2. Nommage des Templates
Utilisez toujours la convention `nom_addon.NomComposant`.
Cela évite les collisions de noms entre addons (ex: deux addons définissant un template "Dashboard").

## 3. Conformité ES2019
N'utilisez pas de fonctionnalités JS trop récentes non supportées par les navigateurs cibles (sauf si transpilées). Le code JS Odoo doit être "Ecmascript 2019 compliant".
Par exemple, la définition de propriétés statiques sans mot clé `static` (champs de classe) peut varier selon les chaînes de build, mais Odoo supporte `static template = ...`.
