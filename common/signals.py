from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    if sender.name != 'common':
        return

    groups = {
        'Super Admin': {
            'permissions': Permission.objects.all()
        },
        'Staff Admin': {
            'model_perms': ['add', 'change', 'delete'],
            'models': ['workoutplan', 'mealplan', 'recipe']
        }
    }

    for group_name, opts in groups.items():
        group, created = Group.objects.get_or_create(name=group_name)
        if 'permissions' in opts:
            perms = opts['permissions']
        else:
            perms = []
            for model in opts['models']:
                ctype = ContentType.objects.get(app_label='common', model=model)
                for action in opts['model_perms']:
                    perms.append(Permission.objects.get(content_type=ctype, codename=f"{action}_{model}"))
        group.permissions.set(perms)
        group.save()
