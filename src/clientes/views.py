from django.shortcuts import render

from clientes.models import Cliente

# Create your views here.
def index(request):
    cliente = Cliente.objects.all()
    contexto = {"clientes": cliente}
    return render(request, "clientes/index.html", contexto)