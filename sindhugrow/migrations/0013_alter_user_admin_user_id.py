# Generated by Django 4.1.7 on 2023-03-28 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sindhugrow', '0012_user_admin_delete_adminuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_admin',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sindhugrow.usermaster'),
        ),
    ]
