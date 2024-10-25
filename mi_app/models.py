from django.db import models
from django.core.exceptions import ValidationError

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField(null=True, blank=True)
    anio = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='peliculas/', blank=True, null=True)  # Guardar en 'media/peliculas/'

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
