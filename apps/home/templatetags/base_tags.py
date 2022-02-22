from django import template
from domain.models import Navbar
import json

from domain.serializers import NavbarsSerializer

register = template.Library()


@register.inclusion_tag('home/partials/recursive.html')
def navbars():
    navbars = NavbarsSerializer(Navbar.objects.filter(parent__isnull=True), many=True).data
    navbars = list(navbars)
    return {'menu':navbars}

