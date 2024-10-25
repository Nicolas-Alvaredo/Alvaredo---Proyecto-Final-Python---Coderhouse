from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, EditarPerfilForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import DatosExtra
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Vista de registro usando CBV
class RegisterView(CreateView):
    template_name = 'login/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login:login')

    def form_valid(self, form):
        # Guarda el usuario y luego redirige al login con mensaje de éxito
        response = super().form_valid(form)
        messages.success(self.request, 'Usuario registrado exitosamente. ¡Ahora puedes iniciar sesión!')
        return response

# Vista de login usando CBV
class CustomLoginView(LoginView):
    template_name = 'login/login.html'

# Vista de logout usando CBV
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('mi_app:inicio')

# Vista de edición de perfil usando CBV
class EditarPerfilView(LoginRequiredMixin, UpdateView):
    template_name = 'login/editar_perfil.html'
    form_class = EditarPerfilForm
    success_url = reverse_lazy('mi_app:inicio')

    def get_object(self):
        # Obtiene el usuario actual y crea DatosExtra si no existe
        user = self.request.user
        DatosExtra.objects.get_or_create(user=user)  # Asegura que DatosExtra exista
        return user

    def form_valid(self, form):
        # Guarda el avatar si fue subido
        avatar = form.cleaned_data.get('avatar')
        if avatar:
            datos_extra = get_object_or_404(DatosExtra, user=self.request.user)
            datos_extra.avatar = avatar
            datos_extra.save()
        return super().form_valid(form)
    
# Vista para cambiar contraseña usando CBV
class CambiarPasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'login/cambiar_password.html'
    success_url = reverse_lazy('mi_app:inicio')  # Redirigir al inicio

    def form_valid(self, form):
        """Envía mensaje de éxito y redirige al inicio."""
        messages.success(self.request, '¡Contraseña cambiada exitosamente!')
        return super().form_valid(form)