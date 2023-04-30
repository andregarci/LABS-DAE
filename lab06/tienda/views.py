from django.shortcuts import get_object_or_404, render
from .models import Categoria,Producto

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')
    lista_categorias = Categoria.objects.all()
    context = {
        'categorias':lista_categorias,
        'product_list': product_list
        }
    
    return render(request,'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request,'producto.html', {'producto' : producto})

def categoria(request,categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    lista_productos = Producto.objects.get(categoria =categoria_id )
    lista_categorias = Categoria.objects.all()
    
    context = {
        'productos':lista_productos,
        'categorias':lista_categorias,
        'categoria':categoria
    }
    
    return render(request,'index.html',context)