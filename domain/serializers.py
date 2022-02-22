from rest_framework import serializers
from domain.models import *
from rest_framework_recursive.fields import RecursiveField

class NavbarsSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)
    class Meta:
        model = Navbar
        fields = ('id','title','children')
        depth=1