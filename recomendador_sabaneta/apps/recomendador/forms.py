from django import forms
from .models import Comercio

class ComercioForm(forms.ModelForm):
    class Meta:
        model = Comercio
        fields = '__all__'