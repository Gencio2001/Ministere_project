from django.shortcuts import render

def liste_structures(request):
    # Pour l'instant, on laisse la liste vide []
    structures = [] 
    return render(request, 'structures/liste.html', {'structures': structures})
def ajouter_structure(request):
    return render(request, 'structures/ajouter_structure.html')