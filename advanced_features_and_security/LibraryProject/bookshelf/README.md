# Permissions & Groups Setup

## Custom Permissions
- `can_view` → Allows viewing user data.
- `can_create` → Allows creating user data.
- `can_edit` → Allows editing user data.
- `can_delete` → Allows deleting user data.

## Groups
- **Viewers** → Assigned `can_view`.
- **Editors** → Assigned `can_view`, `can_create`, `can_edit`.
- **Admins** → Assigned all (`can_view`, `can_create`, `can_edit`, `can_delete`).

## Usage
- Permissions enforced using `@permission_required` decorators in views.
- Groups can be managed via Django Admin or assigned programmatically.
