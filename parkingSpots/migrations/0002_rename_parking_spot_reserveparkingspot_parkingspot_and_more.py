# Generated by Django 4.2.3 on 2023-07-07 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkingSpots', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserveparkingspot',
            old_name='parking_spot',
            new_name='parkingSpot',
        ),
        migrations.RenameField(
            model_name='reserveparkingspot',
            old_name='reserve_user',
            new_name='reserveUser',
        ),
    ]