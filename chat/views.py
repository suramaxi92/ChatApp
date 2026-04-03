from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def room1(request):
    return render(request, 'room1.html')

def room2(request):
    return render(request, 'room2.html')

def room3(request):
    return render(request, 'room3.html')