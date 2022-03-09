from rest_framework import serializers
from domain.models import *
from rest_framework_recursive.fields import RecursiveField

class NavbarsSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)
    page_slug= serializers.SerializerMethodField()
    page_group=serializers.SerializerMethodField()

    def get_page_slug(self,obj):
        if obj.page:
            print(obj.page.page_group.get_type_display())
            return obj.page.page_group.get_type_display()
    def get_page_group(self,obj):
        if obj.page:
            return obj.page.slug
    class Meta:
        model = Navbar
        fields = ('id','title','children','icon','page_slug','page_group')
        depth=1