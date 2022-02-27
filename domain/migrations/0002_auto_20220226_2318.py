# Generated by Django 3.1 on 2022-02-26 19:48

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbar',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='فعال یاشد؟'),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='is_internal_link',
            field=models.BooleanField(default=True, verbose_name='لینک خارجی است؟'),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='is_megamenu',
            field=models.BooleanField(default=False, verbose_name='از نوع مگامنو باشد؟'),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='is_open_new_tab_browser',
            field=models.BooleanField(default=False, verbose_name='باز شدن در تب جدید'),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='لینک'),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='domain.page', verbose_name='انتخاب صفحه'),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='domain.navbar', verbose_name='والد'),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='page',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='بدنه صفحه'),
        ),
        migrations.AlterField(
            model_name='page',
            name='cover',
            field=models.ImageField(upload_to='images/pages', verbose_name='عکس کاور'),
        ),
        migrations.AlterField(
            model_name='page',
            name='description',
            field=models.CharField(max_length=1000, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='page',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.pagegroup', verbose_name='گروه صفحه'),
        ),
        migrations.AlterField(
            model_name='page',
            name='published_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار'),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=450, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='pagegroup',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='pagegroup',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'NEWS'), (1, 'BLOG'), (2, 'ABOUT_ME'), (3, 'CONTACT_US'), (4, 'OTHER')], verbose_name='نوع'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='عنوان')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='domain.category', verbose_name='والد')),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='domain.category', verbose_name='دسته بندی'),
            preserve_default=False,
        ),
    ]
