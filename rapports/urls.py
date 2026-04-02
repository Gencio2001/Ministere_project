from django.urls import path
from . import views

app_name = 'rapports' # C'est le namespace utilisé dans {% url 'rapports:...' %}

urlpatterns = [
    # Le name ici doit être 'liste' pour correspondre à ton template
    path('', views.liste_rapports, name='liste'), 
    
    # Le name ici doit être 'ajouter' pour correspondre à ton template
    path('ajouter/', views.ajouter_rapport, name='ajouter'),
    

]