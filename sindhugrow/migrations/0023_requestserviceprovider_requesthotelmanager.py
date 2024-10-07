# Generated by Django 4.1.7 on 2023-04-02 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sindhugrow', '0022_remove_farmer_status_remove_hotelmanager_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='requestServiceprovider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('village', models.CharField(max_length=50)),
                ('taluka', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=150)),
                ('equipment', models.CharField(max_length=150)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sindhugrow.usermaster')),
            ],
        ),
        migrations.CreateModel(
            name='requestHotelmanager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('hotelcontact', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=500)),
                ('taluka', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=150)),
                ('hotelname', models.CharField(max_length=150)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sindhugrow.usermaster')),
            ],
        ),
    ]
