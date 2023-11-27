from django.shortcuts import render
from django.http import HttpResponse
from .models import Flight, Airport, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
# def index(request):
# return HttpResponse(f'<h1>Hello</h1>')

def index(request):
    return render(request, "flights/index.html", {
    "flights": Flight.objects.all()
 })

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flights=flight).all()
    return render(request, "flights/flight.html", {
    "flight": flight,
    "passengers": passengers,
    "non_passengers": non_passengers
 })


def book(request, flight_id):
    # For a post request, add a new flight
    if request.method == "POST":
        # Accessing the flight
        flight = Flight.objects.get(pk=flight_id)

        passenger_id = int(request.POST['passenger'])

        passenger = Passenger.objects.get(pk=passenger_id)
        passenger.flights.add(flight)
    return HttpResponseRedirect(reverse('flight', args=(flight.id,)))