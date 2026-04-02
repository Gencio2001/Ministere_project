from django.urls import path
from . import views
from .views import liste_recommandations,ajouter_recommandation

app_name = 'recommandations' # Identifiant pour ta base.html

urlpatterns = [
    path('', liste_recommandations, name='liste'),
    path('ajouter/', ajouter_recommandation, name='ajouter'),
]