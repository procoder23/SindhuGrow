# Generated by Django 4.1.7 on 2023-03-27 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sindhugrow', '0005_schemes_link2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schemes',
            name='date',
        ),
        migrations.AlterField(
            model_name='schemes',
            name='publishdate',
            field=models.DateField(),
        ),
    ]
