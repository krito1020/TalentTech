from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # ← Este cambio es clave
    path('registro/', views.registrar_comercio, name='registro'),
]