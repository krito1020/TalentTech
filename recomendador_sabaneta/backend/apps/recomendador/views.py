from django.shortcuts import render, redirect
from .forms import ComercioForm
from .models import Comercio
from .recommender import RecomendadorEmpresas
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_EXCEL = os.path.join(BASE_DIR, '../../data/base_actualizada.xlsx')
recomendador = RecomendadorEmpresas(PATH_EXCEL)

def index(request):
    recomendaciones = None
    if request.method == 'POST':
        consulta = request.POST.get('consulta')
        recomendaciones = recomendador.recomendar(consulta).to_dict(orient='records')
    return render(request, 'index.html', {'recomendaciones': recomendaciones})

def registrar_comercio(request):
    if request.method == 'POST':
        form = ComercioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ComercioForm()
    return render(request, 'registro.html', {'form': form})