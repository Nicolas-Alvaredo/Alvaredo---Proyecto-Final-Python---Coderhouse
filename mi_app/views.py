from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib import messages  # Importar mensajes
from django.shortcuts import render, redirect
from .models import Pelicula
from .forms import PeliculaForm
from django.core.exceptions import ValidationError

class InicioView(TemplateView):
    template_name = 'mi_app/inicio.html'

class AcercaDeMiView(TemplateView):
    template_name = 'mi_app/acerca_de_mi.html'

class PeliculaListView(ListView):
    model = Pelicula
    template_name = 'mi_app/buscar_peliculas.html'
    context_object_name = 'peliculas'

class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = 'mi_app/pelicula_detail.html'

class PeliculaCreateView(TemplateView):
    template_name = 'mi_app/crear_pelicula.html'

    def get(self, request, *args, **kwargs):
        form = PeliculaForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = PeliculaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Película creada con éxito.")  # Mensaje de éxito
                return redirect('pelicula-create')  # Redirigir para limpiar el formulario
            except ValidationError as e:
                error_message = e.message_dict.get('anio', ['Error inesperado'])[0]
                messages.error(request, error_message)  # Mensaje de error

        else:
            # Agregar errores del formulario a los mensajes de error
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)  # Mostrar cada error como un mensaje separado

        return render(request, self.template_name, {'form': form})

class PeliculaUpdateView(UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'mi_app/crear_pelicula.html'
    success_url = reverse_lazy('pelicula-list')

class PeliculaDeleteView(DeleteView):
    model = Pelicula
    template_name = 'mi_app/pelicula_confirm_delete.html'
    success_url = reverse_lazy('pelicula-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Película eliminada con éxito.")
        return super().delete(request, *args, **kwargs)
