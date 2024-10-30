from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib import messages  # Importar mensajes
from django.shortcuts import render, redirect
from .models import Pelicula
from .forms import PeliculaForm
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

# Inicio CBV
class InicioView(TemplateView):
    template_name = 'mi_app/inicio.html'
    
# Acerca de Mi CBV
class AcercaDeMiView(TemplateView):
    template_name = 'mi_app/acerca_de_mi.html'

# Buscar Peliculas CBV
class PeliculaListView(LoginRequiredMixin, ListView):
    model = Pelicula
    template_name = 'mi_app/buscar_peliculas.html'
    context_object_name = 'peliculas'

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Obtener los parámetros de búsqueda desde la URL
        titulo = self.request.GET.get('q_titulo', '')
        genero = self.request.GET.get('q_genero', '')
        anio = self.request.GET.get('q_anio', '')

        # Filtrar el queryset basado en los parámetros ingresados
        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)
        if genero:
            queryset = queryset.filter(genero__icontains=genero)
        if anio:
            queryset = queryset.filter(anio=anio)

        return queryset

# Detalles de Peliculas CBV
class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = 'mi_app/pelicula_detail.html'
    context_object_name = 'pelicula'

# Crear Peliculas CBV
class PeliculaCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'mi_app/crear_pelicula.html'

    def get(self, request, *args, **kwargs):
        form = PeliculaForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = PeliculaForm(request.POST, request.FILES)  # Aceptar archivos y datos
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Película creada con éxito.")
                return redirect('mi_app:pelicula-create')
            except ValidationError as e:
                error_message = e.message_dict.get('anio', ['Error inesperado'])[0]
                messages.error(request, error_message)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)

        return render(request, self.template_name, {'form': form})

# Editar Peliculas CBV
class PeliculaUpdateView(UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'mi_app/crear_pelicula.html'
    success_url = reverse_lazy('mi_app:pelicula-list')

    def form_valid(self, form):
        # Verificamos si se seleccionó "Eliminar Imagen"
        if self.request.POST.get('imagen-clear'):
            form.instance.imagen.delete()  # Eliminar imagen del sistema de archivos
            form.instance.imagen = None  # Limpiar el campo en la base de datos
        messages.success(self.request, "Película actualizada con éxito.")
        return super().form_valid(form)




# Eliminar Peliculas CBV
class PeliculaDeleteView(DeleteView):
    model = Pelicula
    template_name = 'mi_app/pelicula_confirm_delete.html'

    def post(self, request, *args, **kwargs):
        pelicula = self.get_object()  # Obtener la película a eliminar
        mensaje = f"La película '{pelicula.titulo}' fue eliminada con éxito."
        pelicula.delete()  # Eliminar la película
        messages.success(request, mensaje)  # Agregar mensaje de éxito
        return HttpResponseRedirect(reverse('mi_app:pelicula-list'))  # Redirigir a la lista