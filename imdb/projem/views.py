from django.shortcuts import render,HttpResponse
from . import models

def index(request):
    return render(request,"index.html")

def film(request):
    return render(request,"film.html") 

def kayit(request):
    return render(request,"kayit.html")  
def uye(request):
    return render(request,"uye.html") 

def tasarim(request):
    return render(request,"tasarim.html") 


# Create your views here.

