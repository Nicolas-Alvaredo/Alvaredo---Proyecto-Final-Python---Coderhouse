# models.py
from django.db import models
from django.core.exceptions import ValidationError

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    anio = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} ({self.anio})"

    def clean(self):
        # Validación: El año no debe ser negativo
        if self.anio < 0:
            raise ValidationError('El año no puede ser negativo.')

    def save(self, *args, **kwargs):
        # Aplicar validaciones antes de guardar
        self.full_clean()  # Asegura que se ejecute la validación personalizada
        super().save(*args, **kwargs)
