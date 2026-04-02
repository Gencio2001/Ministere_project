from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Recommandation 
from core.models import Rapport
from structures.models import Structure
from django.contrib.auth.models import User

def ajouter_recommandation(request):
    if request.method == 'POST':
        # 1. Récupération des données simples
        titre = request.POST.get('titre')
        priorite = request.POST.get('priorite')
        constat = request.POST.get('constat')
        reco_detaillee = request.POST.get('recommandation_detaillee')
        date_echeance = request.POST.get('date_echeance')

        # 2. Récupération des listes d'IDs (ManyToMany)
        rapport_ids = request.POST.getlist('rapport_lie')
        # On récupère l'ID de la structure responsable principale du formulaire
        structure_principale_id = request.POST.get('structure_responsable') 

        try:
            # Génération de la référence
            count = Recommandation.objects.count() + 1
            new_ref = f"REC-{str(count).zfill(4)}"
            
            # CRÉATION : On ne met QUE les champs simples (CharField, TextField, DateField)
            reco = Recommandation.objects.create(
                reference=new_ref,
                titre=titre,
                priorite=priorite,
                constat=constat,
                recommandation_detaillee=reco_detaillee,
                date_echeance=date_echeance if date_echeance else None,
                # Le statut est 'brouillon' par défaut dans le modèle
            )

            # 3. ASSIGNATION DES RELATIONS (ManyToMany se fait APRÈS le .create)
            
            # Rapports liés
            if rapport_ids:
                reco.rapports_lies.set(rapport_ids)
            
            # Structures responsables (ton modèle utilise un ManyToMany ici)
            if structure_principale_id:
                reco.structures_responsables.add(structure_principale_id)

            messages.success(request, "La recommandation a été enregistrée avec succès.")

            if 'save_add' in request.POST:
                return redirect('recommandations:ajouter') 
            else:
                return redirect('recommandations:liste')

        except Exception as e:
            messages.error(request, f"Erreur lors de l'enregistrement : {e}")

    # --- PARTIE GET ---
    context = {
        'rapports': Rapport.objects.all().order_by('-date_debut'),
        'structures': Structure.objects.all(),
        'prochaine_ref': f"REC-{str(Recommandation.objects.count() + 1).zfill(4)}",
    }
    return render(request, 'recommandations/ajouter.html', context)

def liste_recommandations(request):
    # On récupère les données avec prefetch_related pour que la boucle HTML fonctionne
    recommandations = Recommandation.objects.all().prefetch_related('rapports_lies').order_by('-date_creation')
    return render(request, 'recommandations/liste.html', {'recommandations': recommandations})