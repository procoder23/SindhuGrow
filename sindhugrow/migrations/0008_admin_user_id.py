# Generated by Django 4.1.7 on 2023-03-28 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sindhugrow', '0007_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sindhugrow.usermaster'),
        ),
    ]