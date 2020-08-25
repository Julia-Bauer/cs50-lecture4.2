from django.shortcuts import render
from django.http import HttpResponseRedirect
#reverse pega o nome de uma view conforme definido no urls.py
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

#pk = primarykey
def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        #passengers é o ralated name
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)

        #Qual passenger id registrar no voo? (vai procurar algo que o nome do campo no form seja passenger)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))

        passenger.flights.add(flight)

        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))