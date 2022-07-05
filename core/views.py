from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt
from crud.models import *

# Create your views here.
def root(request):
    return redirect('/home')

def home(request):
    return render(request,"core/home.html")
def info(request):
    return render(request,"core/info.html")

def nosotros(request):
    context =   { 'empleados': Empleado.objects.all()} 
    return render(request,"core/nosotros.html",context)

def ubicacion(request):
    return render(request,"core/ubicacion.html")

def contacto(request):
    return render(request,"core/contacto.html")
def registro(request):
    return render(request,"core/registro.html")


def register(request):
    if request.method == 'GET':
        return redirect('/')
    else:
        if request.method == 'POST':
            errors = User.objects.validador_campos(request.POST)

            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request,value)

                #Si se produce un error pero no queremos perder los datos....
                request.session['registro_nombre'] = request.POST['first_name']
                request.session['registro_apellido'] = request.POST['last_name']
                request.session['registro_email'] = request.POST['email']
                request.session['level_mensaje'] = 'alert-danger'

            else:
                request.session['registro_nombre'] = ""
                request.session['registro_apellido'] = ""
                request.session['registro_email'] = ""

                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                email = request.POST['email']
                password_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

                obj = User.objects.create(first_name=first_name, last_name=last_name,email=email,password=password_hash)
                messages.success(request, "Usuario registrado con éxito!!!!")
                request.session['level_mensaje'] = 'alert-success'
            
            return redirect('/')

        return render(request, 'core/login.html')
            
            
def login(request):
    if request.method == 'GET':
        return redirect("/")
    else:
        if request.method == 'POST':
            
            user = User.objects.filter(email=request.POST['email_login']) #Buscamos el correo ingresado en la BD             
            
            if user : #Si el usuario existe

                usuario_registrado = user[0]
                
                if bcrypt.checkpw(request.POST['password_login'].encode(), usuario_registrado.password.encode()): 
                    usuario = {
                        'id':usuario_registrado.id,
                        'first_name':usuario_registrado.first_name,
                        'last_name':usuario_registrado.last_name,
                        'email':usuario_registrado.email,
                        'rol':usuario_registrado.rol,
                    }

                    request.session['usuario'] = usuario
                    messages.success(request,"Ingreso correcto!!!!")
                    return redirect('/success')
                else:
                    messages.error(request,"Datos mal ingresados o el usuario no existe!!!")
                    return redirect('core/home')
            else:
                messages.error(request,"Datos mal ingresados o el usuario no existe!!!")
                return redirect('core/home')
            
def logout(request):
    if 'usuario' in request.session:
        del request.session['usuario']
    
    return redirect('/')


def success(request):
    if 'usuario' not in request.session:
        return redirect('/')
        
    return render(request, 'core/success.html')

