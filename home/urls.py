from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hakkimizda', views.hakkimizda, name='hakkimizda'),
    path('iletişim', views.iletişim, name='iletişim'),
]
