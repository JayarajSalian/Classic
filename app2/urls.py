from django.urls import path
from app2.views import *
app_name='bike2'
urlpatterns=[
    path('classic/',classic,name='classic')
]