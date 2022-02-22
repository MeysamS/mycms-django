from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions,viewsets
from domain.serializers import *

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