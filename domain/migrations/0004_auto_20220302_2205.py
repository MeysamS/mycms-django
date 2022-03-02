# Generated by Django 3.1 on 2022-03-02 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0003_auto_20220302_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companymember',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'مدیر عامل'), (1, 'رئیس هیأت مدیره'), (2, 'نائب رئیس هیأت مدیره'), (3, 'هیأت مدیره (اصلی)'), (4, 'هیأت مدیره (علل بدل)'), (5, 'بازرس'), (6, 'حسابدار')], verbose_name='سمت'),
        ),
    ]
