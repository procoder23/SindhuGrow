# Generated by Django 4.1.7 on 2023-04-04 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sindhugrow', '0037_remove_usermaster_is_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermaster',
            name='is_active',
        ),
    ]
