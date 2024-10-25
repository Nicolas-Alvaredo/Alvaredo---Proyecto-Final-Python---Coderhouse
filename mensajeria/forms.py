from django import forms
from django.contrib.auth.models import User
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    destinatario = forms.ModelChoiceField(
        queryset=User.objects.all(), 
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Destinatario"
    )
    contenido = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        label="Escribe tu mensaje"
    )

    class Meta:
        model = Mensaje
        fields = ['destinatario', 'contenido']
