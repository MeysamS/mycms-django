# Generated by Django 3.1 on 2022-02-27 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0007_auto_20220226_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagegroup',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'NEWS'), (1, 'BLOG'), (2, 'ABOUT_ME'), (3, 'CONTACT_US'), (4, 'OTHER'), (5, 'OTHER2')], verbose_name='نوع'),
        ),
    ]
