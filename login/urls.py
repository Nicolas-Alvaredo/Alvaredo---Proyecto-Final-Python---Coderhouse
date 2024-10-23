from django.urls import path
from .views import RegisterView, CustomLoginView, CustomLogoutView, EditarPerfilView, CambiarPasswordView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('editar-perfil/', EditarPerfilView.as_view(), name='editar_perfil'),
    path('cambiar-password/', CambiarPasswordView.as_view(), name='cambiar_password'),
]
