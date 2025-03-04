from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate

class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

    def ready(self):
        post_migrate.connect(create_groups_and_permissions, sender=self)

def create_groups_and_permissions(sender, **kwargs):
    from .models import Book  # Import your model

    content_type = ContentType.objects.get_for_model(Book)

    # Define required permissions
    permissions = {
        "can_view": Permission.objects.get(codename="can_view", content_type=content_type),
        "can_create": Permission.objects.get(codename="can_create", content_type=content_type),
        "can_edit": Permission.objects.get(codename="can_edit", content_type=content_type),
        "can_delete": Permission.objects.get(codename="can_delete", content_type=content_type),
    } 
    
    groups_permissions = {
        "Admins": permissions.values(),  # Admins get all permissions
        "Editors": [permissions["can_view"], permissions["can_create"], permissions["can_edit"]],
        "Viewers": [permissions["can_view"]],
    }

    # Create groups and assign permissions
    for group_name, perms in groups_permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        group.permissions.set(perms)