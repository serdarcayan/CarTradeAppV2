from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('profile', views.profile, name='profil'),
    path('register', views.user_register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('favori-ilanlar', views.favilanlar, name='favilanlar'),
    path('ilan-olustur', views.ilanolustur, name='ilanolustur'),
]
