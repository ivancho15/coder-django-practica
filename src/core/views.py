from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def saludar(request):
        return HttpResponse("Hola desde Django")

def saludar2(request):
        return HttpResponse("<H1>Esta es el titulo</H1>")

def saludar3(request, nombre: str, apellido: str):
        nombre = nombre.upper()
        apellido = apellido.capitalize()
        return HttpResponse(f"{apellido}, {nombre}")

def index(request):
        ahora = datetime.now()
        contexto = {
                "fecha":ahora
        }
        return render(request, "core/index.html", contexto)
