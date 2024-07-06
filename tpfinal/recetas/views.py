from django.shortcuts import render

# Create your views here.

def recetas(request):
    return render(request, "recetas/recetas.html")