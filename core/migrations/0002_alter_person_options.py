# Generated by Django 5.0.6 on 2024-06-27 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('last_name', 'first_name'), 'verbose_name_plural': 'People'},
        ),
    ]
