from django.urls import path
from app1.views import *
app_name='something'
urlpatterns=[
    path('samplem/',samplem,name='samplem'),
    path('samplen/',samplen,name='samplen'),
]