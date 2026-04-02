from django.urls import path
from . import views

# On ne met pas d'app_name ici pour l'accueil 
# afin que {% url 'home' %} fonctionne simplement partout.

urlpatterns = [
    # Cette ligne capte l'URL vide (http://127.0.0.1:8000/)
    path('', views.dashboard, name='home'),
]