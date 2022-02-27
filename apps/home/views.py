from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions,viewsets
from domain.serializers import *
from django.views.generic import ListView,DetailView
from domain.models import *

def index(request):
   results = [
       {
           "id":1,
           "title":"ریاست",
           "children":[
               {
                   "id": 2,
                   "title":'معاونت',
                   "children":[]
               },
               {
                   "id": 3,
                   "title": 'بازرگانی',
                   "children":[
                       {
                           "id": 45,
                           "title": 'محصولات کشاورزی',
                            "children":[
                                {
                                    "id": 45,
                                    "title": 'محصولات دامی',
                                    "children": []
                                }

                            ]
                       },
                       {
                           "id": 46,
                           "title": 'منابع طبیعی',
                           "children":[]
                       }
                   ]
               },
           ]
       },
       {
           "id": 2,
           "title": "ریاست دوم",
           "children": []
       }
   ]
   navbars = NavbarsSerializer(Navbar.objects.filter(parent__isnull=True), many=True).data
   navbars = list(navbars)
   return render(request,"home/index.html")



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
