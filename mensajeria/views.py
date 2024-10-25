from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect  
from django.contrib import messages
from .forms import MensajeForm
from .models import Mensaje


class EnviarMensajeView(LoginRequiredMixin, CreateView):
    model = Mensaje
    form_class = MensajeForm
    template_name = 'mensajeria/enviar_mensaje.html'
    success_url = reverse_lazy('mensajeria:ver_mensajes')

    def form_valid(self, form):
        mensaje = form.save(commit=False)
        mensaje.remitente = self.request.user  # Asignar remitente al usuario logueado
        mensaje.save()
        messages.success(self.request, 'Mensaje enviado con éxito.')
        # Redirigir con parámetro GET en la URL
        return redirect(f"{self.success_url}?enviado=True")


class VerMensajesView(LoginRequiredMixin, ListView):
    template_name = 'mensajeria/ver_mensajes.html'
    context_object_name = 'recibidos'

    def get_queryset(self):
        # Mensajes recibidos, ordenados del más reciente al más antiguo
        return Mensaje.objects.filter(destinatario=self.request.user).order_by('-fecha_envio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Mensajes enviados, ordenados del más reciente al más antiguo
        context['enviados'] = Mensaje.objects.filter(remitente=self.request.user).order_by('-fecha_envio')
        context['mensaje_exito'] = self.request.GET.get('enviado', False)  # Mensaje de éxito opcional
        return context
    
class EliminarMensajeView(LoginRequiredMixin, DeleteView):
    model = Mensaje
    template_name = 'mensajeria/confirmar_eliminar.html'
    success_url = reverse_lazy('mensajeria:ver_mensajes')

    def get_queryset(self):
        # Asegurar que solo pueda eliminar mensajes relacionados con el usuario
        return Mensaje.objects.filter(
            remitente=self.request.user) | Mensaje.objects.filter(destinatario=self.request.user)

