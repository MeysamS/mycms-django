from django.contrib import admin
from .models import *


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Navbar)
class NavbarAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(PageGroup)
class PageGroupAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ("title",)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("title",)
    autocomplete_fields = ('page',)


@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)
