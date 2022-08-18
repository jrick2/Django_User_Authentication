from django.shortcuts import render

from main.models import flight

# Create your views here.

def index(request):
    return render(request, "main/index.html", {
        "flight": flight.objects.all()
    })

def flights(request, flight_id):
    flight = flight.objects.get(pk=flight_id)
    return render(request, "main/flight.html", {
        "flights":flight,
        "passengers": flight.passengers.all()
    })