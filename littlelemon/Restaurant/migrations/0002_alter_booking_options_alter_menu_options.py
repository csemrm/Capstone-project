# Generated by Django 4.2.3 on 2023-07-26 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Booking'},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'Menu'},
        ),
    ]
