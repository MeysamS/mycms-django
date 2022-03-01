from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions,viewsets
from domain.serializers import *
from django.views.generic import ListView,DetailView
from domain.models import *


def index(request):
   # navbars = NavbarsSerializer(Navbar.objects.filter(parent__isnull=True), many=True).data
   # navbars = list(navbars)
   sliders = Slider.objects.all()
   services = Services.objects.all()
   last_news = Page.objects.all()[:10]
   return render(request,"home/index.html",context={
       'sliders':sliders,
       'services':services,
       'last_news':last_news
   })


class NavbarViewSet(viewsets.ModelViewSet):
    queryset = Navbar.objects.filter(parent__isnull=True)
    serializer_class = NavbarsSerializer


class Blogs(ListView):
    model = Page
    queryset = Page.objects.all()
    template_name = 'home/blogs.html'
    paginate_by = 5
    ordering = '-created_at'
    extra_context = {
        'categories':Category.objects.all(),
        'last_blogs':Page.objects.order_by('-created_at')[:5],
        'tags':Tag.objects.all()[:5],
    }


class BlogDetail(DetailView):
    model = Page
    template_name = 'home/detail.html'
    extra_context = {
        'categories':Category.objects.all(),
        'last_blogs':Page.objects.order_by('-created_at')[:5],
        'tags':Tag.objects.all()[:5],
    }
