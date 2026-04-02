from django.shortcuts import render

def liste_utilisateurs(request):
    # RG-046: Affichage des comptes par rôle et structure
    utilisateurs = [] 
    
    context = {
        'utilisateurs': utilisateurs,
        'roles_disponibles': [
            'Administrateur', 'Coordonnateur CCI-SPSM', 'Délégué', 
            'Responsable CSR-SGM', 'Visualisateur'
        ]
    }
    return render(request, 'users/liste.html', context)

def connexion(request):
    # RG-043: Formulaire d'accès sécurisé
    return render(request, 'users/login.html')