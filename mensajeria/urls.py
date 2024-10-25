from django.urls import path
from .views import EnviarMensajeView, VerMensajesView, EliminarMensajeView

app_name = 'mensajeria'

urlpatterns = [
    path('enviar/', EnviarMensajeView.as_view(), name='enviar_mensaje'),
    path('ver/', VerMensajesView.as_view(), name='ver_mensajes'),
    path('eliminar/<int:pk>/', EliminarMensajeView.as_view(), name='eliminar_mensaje'),
]
