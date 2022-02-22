from django.contrib import admin
from .models import Navbar, Page, PageGroup, Slider


@admin.register(Navbar)
class NavbarAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(PageGroup)
class PageGroupAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("title",)
