from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('grants/', grant_list, name='grants'),
    path('programs/', program_list, name='programs'),
    path('program/detail/<int:pk>', program_detail, name='program_detail'),
    path('grant/detail/<int:pk>', grant_detail, name='grant_detail'),
]
