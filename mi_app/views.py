from django.shortcuts import render, redirect
from .forms import PeliculaForm
from .models import Pelicula

# Vista para la página de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Vista para crear una nueva película
def crear_pelicula(request):
    success = False
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            success = True  # Indicar que la película fue creada con éxito
            form = PeliculaForm()  # Reiniciar el formulario para que quede vacío
    else:
        form = PeliculaForm()
    return render(request, 'crear_pelicula.html', {'form': form, 'success': success})


# Vista para buscar películas
def buscar_peliculas(request):
    titulo_query = request.GET.get('q_titulo')
    genero_query = request.GET.get('q_genero')
    anio_query = request.GET.get('q_anio')
    
    peliculas = Pelicula.objects.all()

    # Filtrar por título
    if titulo_query:
        peliculas = peliculas.filter(titulo__icontains=titulo_query)
    
    # Filtrar por género
    if genero_query:
        peliculas = peliculas.filter(genero__icontains=genero_query)
    
    # Filtrar por año
    if anio_query:
        peliculas = peliculas.filter(anio=anio_query)
    
    return render(request, 'buscar_peliculas.html', {'peliculas': peliculas})


# Vista para la página "Acerca de mí"
def acerca_de_mi(request):
    return render(request, 'acerca_de_mi.html')
