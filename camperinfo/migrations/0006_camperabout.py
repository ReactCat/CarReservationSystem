# Generated by Django 4.1.1 on 2022-09-28 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camperinfo', '0005_camper_carnavi_camperjpn_carnavi'),
    ]

    operations = [
        migrations.CreateModel(
            name='CamperAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tit1', models.CharField(max_length=25)),
                ('content1', models.CharField(max_length=255)),
                ('tit2', models.CharField(max_length=25)),
                ('content2', models.TextField(max_length=255)),
                ('tit3', models.CharField(max_length=25)),
                ('content3', models.TextField(max_length=255)),
                ('tit4', models.CharField(max_length=25)),
                ('content4', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name': 'camperabout',
                'verbose_name_plural': 'About Info',
            },
        ),
    ]
