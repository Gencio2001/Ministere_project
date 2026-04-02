from django.shortcuts import render

def liste_journaux(request):
    # On met une liste vide [] pour déclencher le bloc {% empty %} du template
    logs = [] 
    
    return render(request, 'journaux/liste.html', {'logs': logs})