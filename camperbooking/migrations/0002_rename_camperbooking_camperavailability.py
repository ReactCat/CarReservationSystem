# Generated by Django 4.1.1 on 2022-09-24 04:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camperinfo', '0005_camper_carnavi_camperjpn_carnavi'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('camperbooking', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Camperbooking',
            new_name='CamperAvailability',
        ),
    ]
