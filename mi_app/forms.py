from django import forms
from .models import Pelicula

class PeliculaForm(forms.ModelForm):
    fecha_lanzamiento = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )

    imagen = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'style': 'display: none;'  # Ocultamos la interfaz predeterminada.
        }),
        label=''
    )

    class Meta:
        model = Pelicula
        fields = ['titulo', 'genero', 'fecha_lanzamiento', 'anio', 'descripcion', 'imagen']
