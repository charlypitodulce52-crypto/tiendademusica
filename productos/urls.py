from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name='inicio'),
    path('productos/', views.listar_productos, name='productos'),
    path('categoria/<str:tipo>/', views.filtrar_categoria, name='filtrar_categoria'),
    path('ofertas/', views.ofertas, name='ofertas'),
]