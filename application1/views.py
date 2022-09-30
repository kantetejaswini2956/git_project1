from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def firstFbv(request):
    return HttpResponse("<h1>Teju</h1>")
