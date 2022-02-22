from django.urls import path
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'navabrs_rest', NavbarViewSet)


urlpatterns = [
    path('',index),
] +router.urls

