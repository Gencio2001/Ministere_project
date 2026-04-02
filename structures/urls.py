# structures/urls.py
from django.urls import path
from .views import liste_structures,ajouter_structure


# C'EST CETTE LIGNE QUI MANQUE :
app_name = 'structures' 


urlpatterns = [
    path('', liste_structures, name='liste'), # Sera accessible via /structures/
    path('ajouter/', ajouter_structure, name='ajouter'),
]