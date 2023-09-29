from django.urls import path
from .views import index,curd,profilSow,delete,updet

urlpatterns = [
    path('', index,name='index'),
    path('curd/', curd, name='curd'),
    path('delete/ <int:id>',delete,name='delete'),
    path('profilSow/ <int:id>',profilSow, name='profilSow'),
    path('updet/<int:id>', updet, name='updet'),
    
]