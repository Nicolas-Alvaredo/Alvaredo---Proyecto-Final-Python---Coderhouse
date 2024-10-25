from django import forms
from .models import Pelicula

class PeliculaForm(forms.ModelForm):
    fecha_lanzamiento = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )

    class Meta:
        model = Pelicula
        fields = ['titulo', 'genero', 'fecha_lanzamiento', 'anio', 'descripcion', 'imagen']
