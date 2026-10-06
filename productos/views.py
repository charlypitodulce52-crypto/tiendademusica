from django.shortcuts import render
from .models import Producto

def listar_productos(request):
    # Consultamos la base de datos para traer todos los productos
    productos = Producto.objects.all()
    # Los enviamos a la plantilla index.html dentro de un diccionario
    return render(request, 'productos/index.html', {'productos': productos})
