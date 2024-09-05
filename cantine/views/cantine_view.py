from django.shortcuts import render,redirect



def index(request):
     # Logique pour préparer le contexte si nécessaire
    context = {}  # Ajoute des données au contexte si besoin
    return render(request, "cantine/index.html", context)
    