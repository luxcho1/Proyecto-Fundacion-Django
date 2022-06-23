from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def root(request):
    return redirect('/home')

def home(request):
    return render(request,"core/home.html")
def info(request):
    return render(request,"core/info.html")

def nosotros(request):
    return render(request,"core/nosotros.html")

def ubicacion(request):
    return render(request,"core/ubicacion.html")

def contacto(request):
    return render(request,"core/contacto.html")