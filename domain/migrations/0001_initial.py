# Generated by Django 3.1 on 2022-03-02 18:18

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='عنوان')),
                ('cover', models.ImageField(upload_to='images/pages', verbose_name='عکس کاور')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ویرایش')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='domain.category', verbose_name='والد')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'مدیر عامل'), (1, 'رئیس هیأت مدیره'), (2, 'نائب رئیس هیأت مدیره'), (3, 'هیأت مدیره (اصلی)'), (4, 'هیأت مدیره (علل بدل)'), (5, 'بازرس'), (6, 'حسابدار')], verbose_name='نوع شرکت')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='نام')),
                ('mobile_number', models.PositiveSmallIntegerField(verbose_name='شماره همراه')),
                ('registry_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ عضویت')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'فعال'), (1, 'غیرفعال')], verbose_name='وضعیت')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ویرایش')),
            ],
        ),
        migrations.CreateModel(
            name='ExternalLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('url', models.URLField(verbose_name='لینک')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ویرایش')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=450, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='اسلاگ')),
                ('content', ckeditor.fields.RichTextField(verbose_name='بدنه صفحه')),
                ('cover', models.ImageField(upload_to='images/pages', verbose_name='عکس کاور')),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='وضعیت')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='domain.category', verbose_name='دسته بندی')),
            ],
        ),
        migrations.CreateModel(
            name='PageGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='عنوان')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'اخبار'), (1, 'وبلاگ'), (2, 'درباره ما'), (3, 'تماس با ما'), (4, 'سایر')], verbose_name='نوع')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ویرایش')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.CharField(blank=True, max_length=350, null=True)),
                ('icon', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ویرایش')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='عنوان')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ویرایش')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.CharField(blank=True, max_length=350, null=True)),
                ('image', models.ImageField(upload_to='images/slider')),
                ('is_external_link', models.BooleanField(default=False)),
                ('link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ویرایش')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='domain.page')),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='page_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.pagegroup', verbose_name='گروه صفحه'),
        ),
        migrations.AddField(
            model_name='page',
            name='tags',
            field=models.ManyToManyField(related_name='pages', to='domain.Tag', verbose_name='برچسب'),
        ),
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='عنوان')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال یاشد؟')),
                ('is_megamenu', models.BooleanField(default=False, verbose_name='از نوع مگامنو باشد؟')),
                ('is_internal_link', models.BooleanField(default=True, verbose_name='لینک خارجی است؟')),
                ('link', models.URLField(blank=True, null=True, verbose_name='لینک')),
                ('is_open_new_tab_browser', models.BooleanField(default=False, verbose_name='باز شدن در تب جدید')),
                ('position', models.SmallIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ویرایش')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='domain.page', verbose_name='انتخاب صفحه')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='domain.navbar', verbose_name='والد')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.CharField(blank=True, max_length=350, null=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'تعاونی روستایی'), (1, 'تعاونی کشاورزی'), (2, 'تعاونی تولید '), (3, 'اتحادیه تعاونی روستایی'), (4, 'اتحادیه تعاونی تولید'), (5, 'نظام صنفی')], verbose_name='نوع شرکت')),
                ('date_of_build', models.PositiveSmallIntegerField(verbose_name='تاریخ ساخت')),
                ('register_number', models.PositiveSmallIntegerField(verbose_name='شماره ثبت')),
                ('national_code', models.PositiveSmallIntegerField(verbose_name='شماره کد ملی')),
                ('economic_code', models.PositiveSmallIntegerField(verbose_name='کد اقتصادی')),
                ('phone_number', models.PositiveSmallIntegerField(verbose_name='تلفن ثابت')),
                ('member_count', models.PositiveSmallIntegerField(verbose_name='تعداد اعضاء')),
                ('village_count', models.PositiveSmallIntegerField(verbose_name='تعداد روستاهای حوزه عمل')),
                ('oil_position_count', models.PositiveSmallIntegerField(verbose_name='تعداد جایگاه مواد نفتی')),
                ('fuel_store_count', models.PositiveSmallIntegerField(verbose_name='تعداد فروشندگی های سوخت')),
                ('last_fund_count', models.PositiveSmallIntegerField(verbose_name='تعداد سهام و آخرین سرمایه ثبتی')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'فعال'), (1, 'غیرفعال')], verbose_name='وضعیت شرکت')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ویرایش')),
                ('companyMember', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='domain.companymember', verbose_name='مدیریت')),
            ],
        ),
    ]
