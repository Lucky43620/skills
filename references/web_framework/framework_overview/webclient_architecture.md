# WebClient Architecture

> Doc officielle : https://www.odoo.com/documentation/19.0/fr/developer/reference/frontend/framework_overview.html#webclient-architecture

## TL;DR

Le WebClient est une application Owl définie par le template `web.WebClient`.

## Structure du Template

```xml
<t t-name="web.WebClient">
    <body class="o_web_client">
        <NavBar/>
        <ActionContainer/>
        <MainComponentsContainer/>
    </body>
</t>
```

- **NavBar** : Barre de navigation supérieure.
- **ActionContainer** : Composant "Higher Order" qui affiche le contrôleur de l'action courante (vue ou client action). Gère le breadcrumb et la coordination.
- **MainComponentsContainer** : Affiche les composants enregistrés dans le registre `main_components`.

## Point d'extension

Le `MainComponentsContainer` est le point d'entrée pour ajouter des composants globaux à l'interface (Dialogs, Notifications, Systray items étendus, Tours, etc.) via le registre `main_components`.
