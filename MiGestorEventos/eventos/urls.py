from django.urls import path
from .views import OrganizadorListView, OrganizadorCreateView, EventoListView, EventoCreateView
from .views import OrganizadorListView, OrganizadorCreateView, EventoListView, EventoCreateView, EventoUpdateView, home
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name='home'),  # Página de inicio
    path('organizadores/', OrganizadorListView.as_view(), name='organizador-list'),
    path('organizadores/nuevo/', OrganizadorCreateView.as_view(), name='organizador-create'),
    path('eventos/', EventoListView.as_view(), name='evento-list'),
    path('eventos/nuevo/', EventoCreateView.as_view(), name='evento-create'),
    path('eventos/<int:pk>/editar/', EventoUpdateView.as_view(), name='evento-update'),  
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
