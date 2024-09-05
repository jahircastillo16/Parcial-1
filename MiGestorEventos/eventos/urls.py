from django.urls import path
from .views import OrganizadorListView, OrganizadorCreateView, EventoListView, EventoCreateView

urlpatterns = [
    path('organizadores/', OrganizadorListView.as_view(), name='organizador-list'),
    path('organizadores/nuevo/', OrganizadorCreateView.as_view(), name='organizador-create'),
    path('eventos/', EventoListView.as_view(), name='evento-list'),
    path('eventos/nuevo/', EventoCreateView.as_view(), name='evento-create'),
]
