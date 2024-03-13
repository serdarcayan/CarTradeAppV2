from django.urls import path

from . import views

urlpatterns = [
    path('', views.ilan, name='ilanlar'),
    path('ilanlar', views.ilan, name='ilanlar'), 
    path('<slug:slug>', views.ilan_detayi, name='ilandetayı'), 
]
