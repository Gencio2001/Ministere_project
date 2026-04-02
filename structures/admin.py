from django.contrib import admin
from .models import Structure

@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    # On utilise responsable_nom ici pour correspondre à ton modèle
    list_display = ('code', 'nom', 'type_structure', 'responsable_nom', 'est_operationnelle', 'date_creation')
    
    # Filtres pratiques
    list_filter = ('type_structure', 'est_operationnelle', 'departement')
    
    # Recherche rapide
    search_fields = ('code', 'nom', 'responsable_nom')
    
    # Le code est auto-généré, on le met en lecture seule dans le formulaire d'ajout
    readonly_fields = ('code', 'date_creation')