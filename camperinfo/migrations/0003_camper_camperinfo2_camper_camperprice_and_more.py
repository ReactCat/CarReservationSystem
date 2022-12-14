# Generated by Django 4.1.1 on 2022-09-23 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camperinfo', '0002_alter_camper_options_alter_camperjpn_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='camper',
            name='camperinfo2',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='camper',
            name='camperprice',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='camperjpn',
            name='camperinfo2',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='camperjpn',
            name='camperprice',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=8),
        ),
    ]
