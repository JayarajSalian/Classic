from django.urls import path
from app1.views import *
app_name='bike'
urlpatterns=[
    path('bullet/',bullet,name='bullet')
]