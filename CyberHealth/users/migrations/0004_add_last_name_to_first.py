from django.db import migrations
from django.contrib.auth import get_user_model


def add_last_name_to_first(apps, schema_editor):
    User = get_user_model()
    users = User.objects.all()
    for user in users:
        name = str(user.first_name)
        if user.last_name:
            name = f'{name} {user.last_name}'
            user.first_name = name
            user.last_name = ""
        user.save()


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('users', '0002_load_init_data'),
    ]

    operations = [
        migrations.RunPython(add_last_name_to_first),
    ]