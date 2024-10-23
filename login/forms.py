from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User



# Formulario de creacion de User
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido. Ingrese un email válido.')
    first_name = forms.CharField(required=True, max_length=30, help_text='Requerido.')
    last_name = forms.CharField(required=True, max_length=30, help_text='Requerido.')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        help_texts = {key: '' for key in fields}
        

# Formulario de edicion de User
class EditarPerfilForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)
    avatar = forms.ImageField(required=False)
    
    password = None  # Esto oculta la sección de contraseña

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'avatar']
