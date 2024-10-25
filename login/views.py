from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, EditarPerfilForm
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import DatosExtra
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect


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
    
# Vista de detalle de Usuario usando CBV  
class VerPerfilView(LoginRequiredMixin, DetailView):
    model = DatosExtra
    template_name = 'login/ver_perfil.html'
    context_object_name = 'perfil'

    def get_object(self):
        # Asegura que cada usuario tenga un perfil y lo devuelve
        return DatosExtra.objects.get_or_create(user=self.request.user)[0]

# Vista de edición de perfil usando CBV
class EditarPerfilView(LoginRequiredMixin, UpdateView):
    template_name = 'login/editar_perfil.html'
    form_class = EditarPerfilForm
    success_url = reverse_lazy('login:ver_perfil')

    def get_object(self):
        # Asegura que el objeto DatosExtra exista para el usuario
        user = self.request.user
        DatosExtra.objects.get_or_create(user=user)
        return user

    def get_form_kwargs(self):
        # Pasar el usuario al formulario
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        # Guardar los datos adicionales si fueron proporcionados
        return super().form_valid(form)

    
# Vista para cambiar contraseña usando CBV
class CambiarPasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'login/cambiar_password.html'
    success_url = reverse_lazy('login:ver_perfil')  # Redirigir al perfil

    def form_valid(self, form):
        """Envía mensaje de éxito y redirige al perfil."""
        messages.success(self.request, '¡Contraseña cambiada exitosamente!')
        return HttpResponseRedirect(self.get_success_url())  # Redirige a perfil con mensaje