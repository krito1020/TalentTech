from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='recomendador_home'),  # ← Este cambio es clave
    path('registro/', views.registrar_comercio, name='registro'),
]