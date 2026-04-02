from django.shortcuts import render

def ajouter_affectations(request):
    return render(request, 'affectations/ajouter.html')

def liste_affectations(request):
    # Liste vide pour le test
    affectations = [] 
    return render(request, 'affectations/liste.html', {'affectations': affectations})