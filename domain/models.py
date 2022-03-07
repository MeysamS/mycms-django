# from turtle import title
from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

PAGE_TYPES_CHOICES = [
    (0, "اخبار"),
    (1, "اطلاعیه ها"),
    (2, "مطالب آموزشی"),
    (4, "درباره ما"),
    (5, "تماس با ما"),
    (6, "سایر"),
]

COMPANY_TYPES_CHOICES = [
    (0, "تعاونی روستایی"),
    (1, "تعاونی کشاورزی"),
    (2, "تعاونی تولید "),
    (3, "اتحادیه تعاونی روستایی"),
    (4, "اتحادیه تعاونی تولید"),
    (5, "نظام صنفی"),
]

POST_TYPES_CHOICES = [
    (0, "مدیر عامل"),
    (1, "رئیس هیأت مدیره"),
    (2, "نائب رئیس هیأت مدیره"),
    (3, "هیأت مدیره (اصلی)"),
    (4, "هیأت مدیره (علل بدل)"),
    (5, "بازرس"),
    (6, "حسابدار"),
]

ACTIVITY_STATUS_CHOICES = [
    (0, "فعال"),
    (1, "غیرفعال"),
]


class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True,verbose_name="عنوان")
    created_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ویرایش')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب'


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True,verbose_name="عنوان")
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="children", blank=True, null=True, verbose_name="والد"
    )
    cover = models.ImageField(
        upload_to="images/pages", verbose_name="عکس کاور"
    )
    created_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ویرایش')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی'


class PageGroup(models.Model):
    title = models.CharField(max_length=100, unique=True,verbose_name="عنوان")
    type = models.PositiveSmallIntegerField(choices=PAGE_TYPES_CHOICES,verbose_name="نوع")
    created_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ویرایش')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'گروه بندی صفحه'
        verbose_name_plural = 'گروه بندی صفحه'
        
        
class Page(models.Model):
    title = models.CharField(max_length=450,verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    slug = models.SlugField(max_length=200, unique=True,verbose_name="اسلاگ")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='pages',verbose_name="دسته بندی")
    tags = models.ManyToManyField(Tag,related_name='pages',verbose_name="برچسب")
    content = RichTextField(verbose_name="بدنه صفحه")
    page_group = models.ForeignKey(PageGroup, on_delete=models.CASCADE,verbose_name="گروه صفحه")
    cover = models.ImageField(
        upload_to="images/pages",verbose_name="عکس کاور"
    )
    published_at = models.DateTimeField(default=timezone.now,verbose_name="تاریخ انتشار")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True,verbose_name="وضعیت")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'صفحه'
        verbose_name_plural = 'صفحهات'


class Navbar(models.Model):
    title = models.CharField(max_length=100, unique=True,verbose_name="عنوان")
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="children", blank=True, null=True,verbose_name="والد"
    )
    is_active = models.BooleanField(
        default=False,verbose_name="فعال یاشد؟"
    )
    is_megamenu = models.BooleanField(
        default=False,verbose_name="از نوع مگامنو باشد؟"
    )
    is_internal_link = models.BooleanField(default=True,verbose_name="لینک خارجی است؟")
    link = models.URLField(null=True, blank=True,verbose_name="لینک")
    page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True, blank=True,verbose_name="انتخاب صفحه")
    is_open_new_tab_browser = models.BooleanField(default=False,verbose_name="باز شدن در تب جدید")
    position = models.SmallIntegerField(null=True, blank=True)
    icon = models.CharField(max_length=100,blank=True,null=True, verbose_name='آیکن')
    created_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ویرایش')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'منو'
        verbose_name_plural = 'منوا'

    def get_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'children': [{'id': b.id, 'title': b.title} for b in self.children.all()]}


class Slider(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True, verbose_name='عنوان')
    description = models.CharField(max_length=350, null=True, blank=True, verbose_name='توضیحات')
    page = models.ForeignKey(Page, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='صفحه')
    image = models.ImageField(upload_to="images/slider", verbose_name='تصویر')
    is_external_link = models.BooleanField(default=False, verbose_name='لینک خارجی')
    link = models.URLField(null=True, blank=True, verbose_name='لینک')
    created_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ویرایش')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر'


class Services(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True, verbose_name='عنوان')
    description = models.CharField(max_length=350, null=True, blank=True, verbose_name='توضیحات')
    icon = models.CharField(max_length=100, verbose_name='آیکن', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ویرایش')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'خدمات'
        verbose_name_plural = 'خدمات'


class CompanyMember(models.Model):
    type = models.PositiveSmallIntegerField(choices=POST_TYPES_CHOICES,verbose_name="سمت")
    name = models.CharField(max_length=150, null=True, blank=True, verbose_name='نام')
    mobile_number = models.PositiveSmallIntegerField(verbose_name="شماره همراه")
    registry_date = models.DateTimeField(auto_now=True,verbose_name="تاریخ عضویت")
    company = models.ForeignKey('Company',on_delete=models.SET_NULL,blank=True,null=True,verbose_name='شرکت')
    status = models.PositiveSmallIntegerField(choices=ACTIVITY_STATUS_CHOICES,verbose_name="وضعیت")
    created_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ویرایش')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'عضو'
        verbose_name_plural = 'اعضاء'


class Company(models.Model):
    title = models.CharField(max_length=250, verbose_name='عنوان')
    description = models.CharField(max_length=500, verbose_name='توضیحات')
    type = models.PositiveSmallIntegerField(choices=COMPANY_TYPES_CHOICES, verbose_name="نوع شرکت")
    date_of_build = models.PositiveSmallIntegerField(verbose_name="تاریخ ساخت", null=True, blank=True)
    register_number = models.PositiveSmallIntegerField(verbose_name="شماره ثبت", null=True, blank=True)
    national_code = models.PositiveIntegerField(verbose_name="شماره شناسه ملی", null=True, blank=True)
    economic_code = models.PositiveIntegerField(verbose_name="کد اقتصادی", null=True, blank=True)
    phone_number = models.PositiveSmallIntegerField(verbose_name="تلفن ثابت", null=True, blank=True)
    member_count = models.PositiveSmallIntegerField(verbose_name="تعداد اعضاء", null=True, blank=True)
    village_count = models.PositiveSmallIntegerField(verbose_name="تعداد روستاهای حوزه عمل", null=True, blank=True)
    oil_position_count = models.PositiveSmallIntegerField(verbose_name="تعداد جایگاه مواد نفتی", null=True, blank=True)
    fuel_store_count = models.PositiveSmallIntegerField(verbose_name="تعداد فروشندگی های سوخت", null=True, blank=True)
    last_fund_count = models.PositiveSmallIntegerField(verbose_name="تعداد سهام و آخرین سرمایه ثبتی", null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=ACTIVITY_STATUS_CHOICES,verbose_name="وضعیت شرکت", null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ویرایش')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'شرکت'
        verbose_name_plural = 'شرکت ها'


class ExternalLink(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    url = models.URLField(verbose_name='لینک')
    created_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ویرایش')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'لینک خارجی'
        verbose_name_plural = 'لینک خارجی'


class Comment(models.Model):
    name = models.CharField(max_length=150, verbose_name='نام نام خانوادگی')
    description = models.CharField(max_length=500)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    phone_number = models.PositiveIntegerField(verbose_name="شماره همراه", null=True, blank=True)
    email = models.EmailField(verbose_name="آدرس الکترونیکی", null=True, blank=True)
    job = models.CharField(max_length=150,verbose_name="شغل", null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=ACTIVITY_STATUS_CHOICES,verbose_name="وضعیت")
    created_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ویرایش')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دیدگاه'
        verbose_name_plural = 'دیدگاه'


class SocialNetwork(models.Model):
    name = models.CharField(max_length=150, verbose_name='نام')
    icon = models.CharField(max_length=100, verbose_name='آیکن')
    link = models.URLField(verbose_name="لینک")

    created_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ویرایش')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'شبکه های اجتماعی'
        verbose_name_plural = 'شبکه های اجتماعی'