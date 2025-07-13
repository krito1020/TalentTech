from django.contrib import admin
from django.urls import path
from apps.recomendador import views

urlpatterns = [
    path('', views.index, name='index'),  # Página principal
    path('registro/', views.registrar_comercio, name='registro'),  # Página de registro
]
