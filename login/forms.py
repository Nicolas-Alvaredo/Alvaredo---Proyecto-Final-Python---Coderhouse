from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import DatosExtra


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
    avatar = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        label="Avatar"
    )
    clear_avatar = forms.BooleanField(
        required=False,
        label="Eliminar Avatar"
    )
    fecha_nacimiento = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    )
    biografia = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=False
    )

    password = None  # Ocultar el campo de contraseña

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'avatar']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        # Inicializar campos con valores actuales del usuario
        self.fields['email'].initial = user.email
        self.fields['first_name'].initial = user.first_name
        self.fields['last_name'].initial = user.last_name

        # Obtener datos adicionales (DatosExtra)
        datos_extra = getattr(user, 'datosextra', None)
        if datos_extra:
            self.fields['fecha_nacimiento'].initial = datos_extra.fecha_nacimiento
            self.fields['biografia'].initial = datos_extra.biografia

    def save(self, commit=True):
        user = super().save(commit=False)

        # Guardar datos básicos del usuario
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        # Guardar datos adicionales en DatosExtra
        datos_extra, _ = DatosExtra.objects.get_or_create(user=user)

        if self.cleaned_data.get('clear_avatar'):
            # Si se seleccionó "Eliminar Avatar", borrar el avatar
            datos_extra.avatar.delete(save=False)
            datos_extra.avatar = None
        else:
            # Si se proporcionó un nuevo avatar, guardarlo
            avatar = self.cleaned_data.get('avatar')
            if avatar:
                datos_extra.avatar = avatar

        datos_extra.fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        datos_extra.biografia = self.cleaned_data.get('biografia')

        if commit:
            user.save()
            datos_extra.save()

        return user
