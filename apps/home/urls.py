from django.urls import path
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'navabrs_rest', NavbarViewSet)

app_name = 'domain'
urlpatterns = [
    path('',index),
    path('pages',Blogs.as_view(),name='blogs'),
    # path('pages/detail/<slug:slug>', BlogDetail.as_view(), name='blog-detail'),
    path('pages/<str:group>/detail/<slug:slug>',BlogDetail.as_view(),name='blog-detail'),
] +router.urls

