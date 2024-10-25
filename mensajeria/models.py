from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    contenido = models.TextField(verbose_name="Escribe tu mensaje")
    fecha_envio = models.DateTimeField(default=now)

    def __str__(self):
        return f"De {self.remitente} para {self.destinatario} - {self.fecha_envio.strftime('%d/%m/%Y %H:%M')}"
