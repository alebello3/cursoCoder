from django.shortcuts import render, HttpResponse
from ProyectoWebApp.models import Articulos, Clientes
from ProyectoWebApp.models import pedidos


# Create your views here.

def home(request):
    return render(request, "ProyectoWebApp/home.html")

def servicios(request):

    if request.method == "POST":
        nombre= request.POST["nombre"]
        seccion= request.POST["seccion"]
        precio= request.POST["precio"]
        articulos =Articulos(nombre=nombre, seccion=seccion, precio=precio)
        articulos.save()
        
    return render(request, "ProyectoWebApp/servicios.html")

def tienda(request):

    if request.method == "POST":
        telefono= request.POST["telefono"]
        fecha= request.POST["fecha"]
        entregado= request.POST["entregado"]
        pedido = pedidos(telefono=telefono, fecha=fecha, entregado=entregado)
        pedido.save()


    return render(request, "ProyectoWebApp/tienda.html")

def blog(request):
    return render(request, "ProyectoWebApp/blog.html")

def contacto(request):

    if request.method == "POST":
        nombre= request.POST["nombre"]
        direccion= request.POST["direccion"]
        correo = request.POST["correo"]
        telefono = request.POST["telefono"]
        contacto =Clientes(nombre=nombre, direccion=direccion, correo=correo, telefono=telefono)
        contacto.save()


    return render(request, "ProyectoWebApp/contacto.html")
