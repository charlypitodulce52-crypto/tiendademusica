from django.shortcuts import render
from .models import Producto

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/index.html', {'productos': productos})

def filtrar_categoria(request, tipo):
    # Filtra los productos cuyo nombre contenga el tipo de categoría (ej: "Guitarra")
    productos = Producto.objects.filter(nombre__icontains=tipo)
    return render(request, 'productos/categoria.html', {'productos': productos, 'tipo': tipo})

def ofertas(request):
    # Aquí puedes mostrar productos con descuento o todos por ahora
    productos = Producto.objects.all()
    return render(request, 'productos/ofertas.html', {'productos': productos})