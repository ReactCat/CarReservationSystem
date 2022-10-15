# Generated by Django 4.1.1 on 2022-09-24 04:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('camperinfo', '0005_camper_carnavi_camperjpn_carnavi'),
        ('camperbooking', '0002_rename_camperbooking_camperavailability'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CamperAvailability',
            new_name='CamperBooking',
        ),
        migrations.AlterModelOptions(
            name='camperbooking',
            options={'verbose_name': 'camperbooking', 'verbose_name_plural': 'Camper Booking '},
        ),
    ]
