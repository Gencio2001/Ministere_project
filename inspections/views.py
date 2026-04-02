from django.shortcuts import render

def dashboard(request):
    # Pour l'instant on affiche le template statique
    # Plus tard, on récupérera les données de la base ici
    return render(request, 'inspections/dashboard.html')