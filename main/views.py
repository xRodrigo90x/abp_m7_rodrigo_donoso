from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Producto, Categoria


# Create your views here.


def index(request):
    return render(request,'index.html')


@login_required
def perfil(request):
    return render(request,'perfil.html')


@login_required
def productos(request):

    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    cat_id = request.GET.get('categoria')
    precio_max = request.GET.get('precio_max')

    if cat_id:
        productos = productos.filter(categoria_id=cat_id)
    
    if precio_max:
        productos = productos.filter(precio__lte=precio_max)

    context = {
        'productos': productos,
        'categorias': categorias,
        'categoria_seleccionada': cat_id,
        'precio_max': precio_max,
    }
    return render(request, 'productos.html', context)


def servicios(request):
    return render(request, 'servicios.html')


def crear_usuario(request):
    if request.method == 'POST':
        allowed_fields = ['username', 'password', 'first_name', 'last_name', 'email']
        filtered_data = {k: v for k, v in request.POST.items() if k in allowed_fields}
        
        try:
            User.objects.create_user(**filtered_data)
            messages.success(request, 'Usuario creado con éxito')
        except Exception as e:
            messages.error(request, f'Error: {e}')
            
        return redirect('crear_usuario')
    
    return render(request,'crear_usuario.html')