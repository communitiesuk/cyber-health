# Generated by Django 3.2.3 on 2021-05-18 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0009_auto_20210513_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('intro_text', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]