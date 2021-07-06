from datetime import datetime
from .forms import AppuntamentiForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from .models import Appuntamenti, Saloni, Dipendenti

def home(request):
    return render(request, 'app/base.html')

def pagina_cliente(request):
    saloni = Saloni.objects.all().order_by('-pk')
    context = {"saloni": saloni}
    return render(request, 'app/paginacliente.html', context)

def salone(request):
    appuntamenti = Appuntamenti.objects.all().order_by('-pk')
    context = {"appuntamenti": appuntamenti}
    return render(request, 'app/GestioneSalone.html', context)

def registerPage(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'app/register.html')

def mostrasaloni(request):
    return render(request, 'app/Saloni.html')

def about(request):
    return render(request, 'app/About.html')

def informazionisalone(request, id):
    saloni = get_object_or_404(Saloni, id = id)
    dipendenti = Dipendenti.objects.filter(Salone = saloni)
    context = {"saloni": saloni, "dipendenti": dipendenti}
    return render(request, 'app/InformazioniSalone.html', context)

def contact(request):
    return render(request, 'app/Contact.html')

def prenota_appuntamento(request, id):
    if request.method == "POST":
        form = AppuntamentiForm(request.POST)
        print(request.POST)
        if form.is_valid():
             nuovo_appuntamento = form.save(commit = False)
             nuovo_appuntamento.Id_Salone = get_object_or_404(Saloni, id = id)
             nuovo_appuntamento.save()
             return redirect("informazionisalone", id = id)
    else:
        form = AppuntamentiForm()
        

    Salone = Saloni.objects.get(id = id)
    dipendenti = Dipendenti.objects.filter(Salone = Salone)
    context = {"form": form, "Dipendenti": dipendenti}
    return render(request, "app/creazione_appuntamento.html", context)


def creazione_appuntamento(request):
    if request.method == "POST":
        form = AppuntamentiForm(request.POST)
        if form.is_valid():
             nuovo_appuntamento = form.save()
             return redirect("gestionesalone")
    else:
        form = AppuntamentiForm()

    context = {"form": form}
    return render(request, "app/creazione_appuntamento.html", context)


def eliminazione_appuntamento(request):
    if request.method == "POST":
        form = AppuntamentiForm(request.POST)
        if form.is_valid():
             nuovo_appuntamento = form.save()
             return redirect("gestionesalone")
    else:
        form = AppuntamentiForm()

    context = {"form": form}
    return render(request, "app/creazione_appuntamento.html", context)

