from django.db import models
from django.core.exceptions import ValidationError

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    anio = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} ({self.anio})"

    def clean(self):
        """Validación personalizada para evitar años negativos."""
        if self.anio < 0:
            raise ValidationError({'anio': 'El año no puede ser negativo.'})

    def save(self, *args, **kwargs):
        """Valida y guarda la película."""
        self.full_clean()  # Ejecuta la validación personalizada
        super().save(*args, **kwargs)
