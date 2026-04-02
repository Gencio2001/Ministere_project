from django.urls import path
from . import views
from .views import liste_utilisateurs,connexion

app_name = 'users'

urlpatterns = [
    path('', liste_utilisateurs, name='liste'),
    path('connexion/', connexion, name='login'), # RG-043
]