from django.urls import path
from .views import RegisterView, CustomLoginView, CustomLogoutView, VerPerfilView, EditarPerfilView, CambiarPasswordView

# Namespace de la app
app_name = "login"

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('perfil/', VerPerfilView.as_view(), name='ver_perfil'),
    path('editar-perfil/', EditarPerfilView.as_view(), name='editar_perfil'),
    path('cambiar-password/', CambiarPasswordView.as_view(), name='cambiar_password'),
]
