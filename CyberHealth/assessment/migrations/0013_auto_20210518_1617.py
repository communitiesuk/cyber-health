# Generated by Django 3.2.3 on 2021-05-18 16:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0012_subcontrol'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='control',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='assessment.control'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='positive_answer',
            field=models.BooleanField(default=True),
        ),
    ]
