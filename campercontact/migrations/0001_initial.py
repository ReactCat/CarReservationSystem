# Generated by Django 4.1.1 on 2022-09-24 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookAmityCamper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camper', models.CharField(max_length=27)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('pickup', models.DateTimeField()),
                ('dropoff', models.DateTimeField()),
                ('subject', models.CharField(max_length=27)),
                ('message', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BookAnthonyCamper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camper', models.CharField(max_length=27)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('pickup', models.DateTimeField()),
                ('dropoff', models.DateTimeField()),
                ('subject', models.CharField(max_length=27)),
                ('message', models.CharField(max_length=255)),
            ],
        ),
    ]
