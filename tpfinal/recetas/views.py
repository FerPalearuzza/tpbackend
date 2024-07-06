from django.shortcuts import render
from .models import Receta
# Create your views here.

def recetas(request):
    recetas = Receta.objects.all()
    return render(request, "recetas/recetas.html", {'recetas': recetas})
    #son distintos así se con cual accedo desde el template
    