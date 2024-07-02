from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def historia(request):
    return render(request, "core/historia.html")

def contacto(request):
    return render(request, "core/contacto.html")

'''
def recetas(request):
    return render(request, "core/index.html")

#recetas individuales
def icecoffee(request):
    return render(request, "core/index.html")

def latte(request):
    return render(request, "core/index.html")

def capuccino(request):
    return render(request, "core/index.html")
'''    