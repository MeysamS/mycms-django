# Generated by Django 3.1 on 2022-02-26 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0003_auto_20220226_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cover',
            field=models.ImageField(default=1, upload_to='images/pages', verbose_name='عکس کاور'),
            preserve_default=False,
        ),
    ]