from django.urls import path
from . import views
from.views import liste_journaux

app_name = 'journaux'

urlpatterns = [
    path('', liste_journaux, name='liste'), # RG-110 (Recherche globale)
]