from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    anio = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} ({self.anio})"
