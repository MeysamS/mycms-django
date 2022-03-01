# from turtle import title
from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

PAGE_TYPES_CHOICES = [
    (0, "NEWS"),
    (1, "BLOG"),
    (2, "ABOUT_ME"),
    (3, "CONTACT_US"),
    (4, "OTHER"),
]


class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True,verbose_name="عنوان")

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True,verbose_name="عنوان")
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="children", blank=True, null=True, verbose_name="والد"
    )
    cover = models.ImageField(
        upload_to="images/pages", verbose_name="عکس کاور"
    )
    def __str__(self):
        return self.title


class PageGroup(models.Model):
    title = models.CharField(max_length=100, unique=True,verbose_name="عنوان")
    type = models.PositiveSmallIntegerField(choices=PAGE_TYPES_CHOICES,verbose_name="نوع")

    def __str__(self):
        return self.title


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

    def __str__(self):
        return self.title

    def get_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'children': [{'id': b.id, 'title': b.title} for b in self.children.all()]}


class Slider(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=350, null=True, blank=True)
    page = models.ForeignKey(Page, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to="images/slider")
    is_external_link = models.BooleanField(default=False)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=350, null=True, blank=True)
    icon = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title