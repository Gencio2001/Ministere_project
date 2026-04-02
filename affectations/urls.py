from django.urls import path
from . import views
from .views import liste_affectations, ajouter_affectations

app_name = 'affectations' # Identifiant pour ta base.html

urlpatterns = [
    path('', liste_affectations, name='liste'),
    path('ajouter/', ajouter_affectations, name='ajouter'),
]