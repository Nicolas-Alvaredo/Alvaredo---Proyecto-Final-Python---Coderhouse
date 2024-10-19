from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

# Vista de registro usando CBV
class RegisterView(CreateView):
    template_name = 'login/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Guarda el usuario y luego muestra el mensaje de éxito
        response = super().form_valid(form)
        messages.success(self.request, 'Usuario registrado con éxito. ¡Ya puedes iniciar sesión!')
        return response  # Asegura que el flujo siga y se guarde el usuario correctamente.


# Vista de login usando CBV
class CustomLoginView(LoginView):
    template_name = 'login/login.html'

    def get(self, request, *args, **kwargs):
        """Captura y muestra los mensajes si los hay."""
        message = request.GET.get('message', None)
        if message:
            messages.success(request, message)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Has iniciado sesión correctamente.')
        return super().form_valid(form)

# Vista de logout usando CBV
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('inicio')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'Has cerrado sesión.')
        return super().dispatch(request, *args, **kwargs)
