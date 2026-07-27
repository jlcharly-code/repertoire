
# Fichier : listings/urls.py
from django.urls import path
from . import views

app_name = 'listings'  # Définit le namespace par défaut pour ce fichier

urlpatterns = [
    path('', views.band_list, name='band-list'),
    path('band_list', views.band_list, name='band-list'),
    path('bands/create/', views.band_create, name='band-create'),
    path('bands/<int:id>/', views.band_detail, name='band-detail'),
    path('bands/<int:id>/edit/', views.band_update, name='band-update'),
    path('contact/', views.contact, name='contact'),
    path('email-sent/', views.email_sent, name='email-sent'),
    path('about/', views.about, name='about'),
]# -*- coding: utf-8 -*-

