# Generated by Django 4.1.7 on 2023-04-04 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sindhugrow', '0034_rename_photo_request_service_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hoteldetails',
            old_name='photo',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='request_service',
            old_name='image',
            new_name='photo',
        ),
    ]
