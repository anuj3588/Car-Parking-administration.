# Generated by Django 4.2.3 on 2023-07-07 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingSpots', '0005_alter_spot_latitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='latitude',
            field=models.DecimalField(decimal_places=9, max_digits=16),
        ),
        migrations.AlterField(
            model_name='spot',
            name='longitude',
            field=models.DecimalField(decimal_places=9, max_digits=16),
        ),
    ]
