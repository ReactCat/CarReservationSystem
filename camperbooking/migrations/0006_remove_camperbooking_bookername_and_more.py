# Generated by Django 4.1.1 on 2022-09-24 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camperbooking', '0005_alter_camperbooking2_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camperbooking',
            name='bookername',
        ),
        migrations.RemoveField(
            model_name='camperbooking2',
            name='bookername',
        ),
    ]
