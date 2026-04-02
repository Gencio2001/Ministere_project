from django.contrib import admin
from .models import Recommandation

# Cette ligne dit à Django : "Affiche ce modèle dans l'admin"
@admin.register(Recommandation)
class RecommandationAdmin(admin.ModelAdmin):
    # Les colonnes qui s'afficheront dans la liste
    list_display = ('reference', 'titre', 'priorite', 'statut', 'date_creation')
    
    # Les filtres sur le côté droit
    list_filter = ('priorite', 'statut', 'date_creation')
    
    # La barre de recherche
    search_fields = ('reference', 'titre', 'constat')
    
    # Pour gérer le ManyToMany proprement dans l'admin
    filter_horizontal = ('rapports_lies',)