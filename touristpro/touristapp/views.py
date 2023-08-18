from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def tourist_dashboard(request):
    return render(request,"dashboard.html")

def vara_select(request):
    return render(request,"varanasi_card.html")

def shiri_select(request):
    return render(request,"shiridi_card.html")

def puri_select(request):
    return render(request,"jagannath.html")

def tiru_select(request):
    return render(request,"tirupathi.html")

def ram_select(request):
    return render(request,"rameswaram.html")

def durga_select(request):
    return render(request,"vijayawada.html")