# Generated by Django 4.1.7 on 2023-03-27 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sindhugrow', '0003_alter_news_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schemes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('publishdate', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('is_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_updated', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]