from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import Rapport
from django.contrib.auth.models import User
from structures.models import Structure

def ajouter_rapport(request):
    if request.method == 'POST':
        try:
            # 1. Création de l'objet de base (champs simples uniquement)
            # On ne met pas delegue_id ni structure_inspectee_id ici car ce sont des ManyToMany
            rapport = Rapport(
                reference=request.POST.get('reference'),
                date_debut=request.POST.get('date_debut'),
                date_fin=request.POST.get('date_fin'),
                departement=request.POST.get('departement'),
                commune=request.POST.get('commune'),
                type_inspection=request.POST.get('type_inspection', 'routine'),
                type_structure=request.POST.get('type_structure'),
                emetteur_saisine=request.POST.get('emetteur'),
                date_saisine=request.POST.get('date_saisine') or None,
                moyen_saisine=request.POST.get('moyen_saisine'),
                motif_saisine=request.POST.get('motif_saisine'),
                observations_generales=request.POST.get('observations_generales'),
                statut='BROUILLON'
            )
            rapport.save() # On sauvegarde d'abord pour avoir un ID

            # 2. Enregistrement des relations multiples (ManyToMany)
            
            # Pour les délégués (multiple dans le template)
            delegues_ids = request.POST.getlist('delegue')
            if delegues_ids:
                rapport.delegues.set(delegues_ids)

            # Pour les structures (multiple dans le template sous le nom 'nom_structure')
            structures_ids = request.POST.getlist('nom_structure')
            if structures_ids:
                rapport.structures_inspectees.set(structures_ids)

            # Pour les membres supplémentaires
            membres_ids = request.POST.getlist('membres_supplementaires')
            if membres_ids:
                rapport.membres_supplementaires.set(membres_ids)

            messages.success(request, f"Rapport {rapport.reference} créé avec succès !")
            return redirect('rapports:liste')

        except Exception as e:
            messages.error(request, f"Erreur lors de l'enregistrement : {str(e)}")

    # --- Logique d'affichage (GET) ---
    
    # Calcul de la prochaine référence (RG-58)
    last_r = Rapport.objects.all().order_by('id').last()
    next_num = 1
    if last_r and last_r.reference and '-' in last_r.reference:
        try:
            next_num = int(last_r.reference.split('-')[1]) + 1
        except (IndexError, ValueError):
            next_num = 1
    
    context = {
        'prochaine_ref': f'RI-{next_num:04d}',
        'utilisateurs': User.objects.all().order_by('first_name'),
        'structures': Structure.objects.all().order_by('nom'), # Retiré filter provisoirement pour test
        'departements': ['Alibori', 'Atacora', 'Atlantique', 'Borgou', 'Collines', 'Couffo', 'Donga', 'Littoral', 'Mono', 'Ouémé', 'Plateau', 'Zou'],
        'communes': ['Abomey-Calavi', 'Cotonou', 'Ouidah', 'Porto-Novo', 'Parakou', 'Allada', 'Bohicon', 'Abomey'],
    }
    return render(request, 'rapports/ajouter.html', context)

def liste_rapports(request):
    # Optimisation : prefetch_related pour les ManyToMany (delegues, structures, membres)
    rapports = Rapport.objects.all().prefetch_related(
        'structures_inspectees', 
        'delegues',
        'membres_supplementaires'
    ).order_by('-date_creation')
    
    return render(request, 'rapports/liste.html', {
        'rapports': rapports,
        'total_rapports': rapports.count()
    })