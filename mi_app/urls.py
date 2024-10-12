from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear_pelicula/', views.crear_pelicula, name='crear_pelicula'),
    path('buscar_peliculas/', views.buscar_peliculas, name='buscar_peliculas'),
    path('acerca_de_mi/', views.acerca_de_mi, name='acerca_de_mi'),
]
