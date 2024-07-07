from django.shortcuts import render
from .models import Receta
# Create your views here.

def recetas(request):
    recetas = Receta.objects.all()
    name_receta = recetas[0].name
    primera_receta = recetas[0]
    return render(request, "recetas/recetas.html", {'recetas': recetas, 'name_receta': name_receta, 'priera_receta':primera_receta})
    #son distintos así se con cual accedo desde el template
    