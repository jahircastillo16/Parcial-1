from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Organizador, Evento
from django.shortcuts import render

class OrganizadorListView(ListView):
    model = Organizador
    template_name = 'eventos/organizador_list.html'
    context_object_name = 'organizadores'

class OrganizadorCreateView(CreateView):
    model = Organizador
    fields = ['nombre', 'email']
    template_name = 'eventos/organizador_form.html'
    success_url = reverse_lazy('organizador-list')

class EventoListView(ListView):
    model = Evento
    template_name = 'eventos/evento_list.html'
    context_object_name = 'eventos'

class EventoCreateView(LoginRequiredMixin, CreateView):
    model = Evento
    fields = ['nombre', 'fecha', 'organizador']
    template_name = 'eventos/evento_form.html'
    success_url = reverse_lazy('evento-list')
    login_url = 'login'  # Redirige a la vista de login si no está autenticado

    def form_valid(self, form):
        # Validación personalizada (ejemplo: prohibir ciertas palabras en el nombre)
        nombre = form.cleaned_data['nombre']
        if 'prohibido' in nombre.lower():
            form.add_error('nombre', 'El nombre no puede contener palabras prohibidas.')
            return self.form_invalid(form)
        return super().form_valid(form)

def home(request):
    return render(request, 'eventos/home.html')
