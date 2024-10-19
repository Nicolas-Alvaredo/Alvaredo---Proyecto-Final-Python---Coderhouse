from django.urls import path
from .views import (
    PeliculaListView, PeliculaDetailView, PeliculaCreateView,
    PeliculaUpdateView, PeliculaDeleteView, InicioView, AcercaDeMiView
)

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),  # Inicio
    path('acerca-de-mi/', AcercaDeMiView.as_view(), name='acerca_de_mi'),  # Acerca de mí
    path('peliculas/', PeliculaListView.as_view(), name='pelicula-list'),  # Listado de películas
    path('peliculas/<int:pk>/', PeliculaDetailView.as_view(), name='pelicula-detail'),  # Ver detalle
    path('peliculas/crear/', PeliculaCreateView.as_view(), name='pelicula-create'),  # Crear película
    path('peliculas/<int:pk>/editar/', PeliculaUpdateView.as_view(), name='pelicula-update'),  # Editar película
    path('peliculas/<int:pk>/eliminar/', PeliculaDeleteView.as_view(), name='pelicula-delete'),  # Eliminar película
]
