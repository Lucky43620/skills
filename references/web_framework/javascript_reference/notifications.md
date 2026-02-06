# Notifications (JS)

Notifications (Toasters) are managed by the `notification` service.

## Usage
```javascript
setup() {
    this.notification = useService("notification");
}

showError() {
    this.notification.add("Something went wrong", {
        title: "Error",
        type: "danger", // 'info', 'warning', 'danger', 'success'
        sticky: true,
    });
}
```

## Options
*   `title`: Bold header.
*   `type`: Color scheme.
*   `sticky`: If true, user must dismiss it manually.
*   `className`: Custom CSS class.
