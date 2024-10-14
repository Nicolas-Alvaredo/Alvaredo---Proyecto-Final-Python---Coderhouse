from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear-pelicula/', views.crear_pelicula, name='crear_pelicula'),
    path('buscar-peliculas/', views.buscar_peliculas, name='buscar_peliculas'),
    path('acerca-de-mi/', views.acerca_de_mi, name='acerca_de_mi'),
]
