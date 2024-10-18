from django.shortcuts import render, redirect
from .forms import PeliculaForm
from .models import Pelicula
from django.core.exceptions import ValidationError


# Vista para la página de inicio
def inicio(request):
    return render(request, 'mi_app/inicio.html')

# Vista para crear una nueva película
def crear_pelicula(request):
    success = False
    error_message = None  # Para almacenar mensajes de error
    form = PeliculaForm()  # Inicializamos el formulario para solicitudes GET

    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            try:
                form.save()  # Intentar guardar la película
                success = True  # Película creada con éxito
                form = PeliculaForm()  # Reiniciar el formulario
            except ValidationError as e:
                # Capturar el mensaje de error del modelo
                error_message = e.messages[0]  # Mostrar solo el primer mensaje de error
        else:
            error_message = 'El año no puede ser negativo.'  # Manejar formulario no válido

    return render(request, 'mi_app/crear_pelicula.html', {
        'form': form,
        'success': success,
        'error_message': error_message
    })


# Vista para buscar películas
def buscar_peliculas(request):
    titulo_query = request.GET.get('q_titulo')
    genero_query = request.GET.get('q_genero')
    anio_query = request.GET.get('q_anio')
    error_message = None

    peliculas = Pelicula.objects.all()

    # Filtrar por título
    if titulo_query:
        peliculas = peliculas.filter(titulo__icontains=titulo_query)
    
    # Filtrar por género
    if genero_query:
        peliculas = peliculas.filter(genero__icontains=genero_query)
    
    # Filtrar por año
    if anio_query:
        try:
            anio = int(anio_query)
            if anio < 0:
                raise ValueError('El año no puede ser negativo.')
            peliculas = peliculas.filter(anio=anio)
        except ValueError as e:
            error_message = str(e)

    return render(request, 'mi_app/buscar_peliculas.html', {
        'peliculas': peliculas,
        'error_message': error_message
    })



# Vista para la página "Acerca de mí"
def acerca_de_mi(request):
    return render(request, 'mi_app/acerca_de_mi.html')