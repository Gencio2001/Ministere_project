from django.contrib import admin
from core.models import Rapport

@admin.register(Rapport)
class RapportAdmin(admin.ModelAdmin):
    # 1. Mise à jour des colonnes (On utilise des fonctions pour les ManyToMany)
    list_display = ('reference', 'display_structures', 'display_delegues', 'type_inspection', 'statut', 'date_creation')
    
    # 2. Filtres (Vérifie que 'departement' existe bien dans ton modèle)
    list_filter = ('statut', 'type_inspection', 'departement')
    
    # 3. Recherche (On pointe vers les nouveaux noms au pluriel)
    search_fields = ('reference', 'structures_inspectees__nom', 'delegues__username')
    
    readonly_fields = ('reference', 'date_creation')
    
    # 4. Organisation des champs (On utilise les noms exacts du modèle)
    fieldsets = (
        ('Informations Générales', {
            'fields': ('reference', ('date_debut', 'date_fin'), ('departement', 'commune'), 'type_inspection')
        }),
        ('Équipe', {
            'fields': ('delegues', 'membres_supplementaires') # 'delegues' au pluriel
        }),
        ('Structure & Saisine', {
            'fields': ('structures_inspectees', 'type_structure', 'emetteur_saisine', 'date_saisine', 'moyen_saisine')
        }),
        ('État du Dossier', {
            'fields': ('statut', 'date_creation')
        }),
    )

    # Fonctions pour afficher les listes (ManyToMany) dans le tableau de l'admin
    def display_structures(self, obj):
        return ", ".join([s.nom for s in obj.structures_inspectees.all()])
    display_structures.short_description = 'Structures inspectées'

    def display_delegues(self, obj):
        return ", ".join([u.username for u in obj.delegues.all()])
    display_delegues.short_description = 'Délégués'