# Generated by Django 3.1 on 2022-02-26 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0006_auto_20220226_2352'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]
