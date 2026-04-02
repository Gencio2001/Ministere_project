from django.shortcuts import render
from .models import Rapport 
from django.db.models import Count

def dashboard(request):
    # 1. Correction : On utilise prefetch_related pour les ManyToMany
    # Et on utilise le nom exact du champ défini dans ton models.py
    rapports_recents = Rapport.objects.all().prefetch_related(
        'structures_inspectees'
    ).order_by('-date_creation')[:5]

    # 2. Calculer les compteurs (Assure-toi que les valeurs 'BROUILLON' match ton modèle)
    stats = {
        'total': Rapport.objects.count(),
        'brouillons': Rapport.objects.filter(statut='brouillon').count(), 
    }

    # 3. Contexte
    context = {
        'rapports_recents': rapports_recents,
        'stats': stats,
    }
    
    return render(request, 'dashboard/index.html', context)