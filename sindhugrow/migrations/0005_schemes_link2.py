# Generated by Django 4.1.7 on 2023-03-27 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sindhugrow', '0004_schemes'),
    ]

    operations = [
        migrations.AddField(
            model_name='schemes',
            name='link2',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
