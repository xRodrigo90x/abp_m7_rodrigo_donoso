from .models import Producto, Categoria  # Cambia 'myapp' por el nombre de tu app

PRODUCTOS = [
    {
        'nombre': 'Notebook Gamer Pro',
        'categoria': 'Electrónica',
        'precio': 850000,
        'precio_antes': 950000,
        'descripcion': 'Procesador de última generación, 16GB RAM y tarjeta de video dedicada.',
        'imagen':'https://rimage.ripley.cl/home.ripley/Attachment/WOP/1/2000408778615/image1-2000408778615'
    },
    {
        'nombre': 'Silla Ergonómica Oficina',
        'categoria': 'Hogar',
        'precio': 120000,
        'precio_antes': 150000,
        'descripcion': 'Silla con soporte lumbar ajustable, ideal para largas jornadas de estudio o trabajo.',
        'imagen': 'https://bookstore.cl/4406-large_default/silla-ergonomica-aura.jpg'
    },
    {
        'nombre': 'Audífonos Noise Cancelling',
        'categoria': 'Electrónica',
        'precio': 180000,
        'precio_antes': 210000,
        'descripcion': 'Cancelación de ruido activa y batería de hasta 40 horas de duración.',
        'imagen': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCFDue3JxdnovC97R6Me5mAK7nLbNsLNKDmA&s'
    },
    {
        'nombre': 'Teclado Mecánico RGB',
        'categoria': 'Electrónica',
        'precio': 55000,
        'precio_antes': 75000,
        'descripcion': 'Switches red, retroiluminación personalizable y conexión USB-C.',
        'imagen': 'https://i.ytimg.com/vi/MwbnpN3uVKA/maxresdefault.jpg'
    },
    {
        'nombre': 'Monitor 27" 4K',
        'categoria': 'Electrónica',
        'precio': 320000,
        'precio_antes': 380000,
        'descripcion': 'Panel IPS con colores vibrantes y bordes ultradelgados.',
        'imagen': 'https://http2.mlstatic.com/D_NQ_NP_2X_821913-MLA99466686266_112025-T.webp'
    },
    {
        'nombre': 'Escritorio Elevable',
        'categoria': 'Hogar',
        'precio': 250000,
        'precio_antes': 290000,
        'descripcion': 'Ajuste de altura eléctrico con memoria de posiciones.',
        'imagen': 'https://http2.mlstatic.com/D_NQ_NP_2X_924458-MLC101109597267_122025-F.webp'
    }
]

def cargar_data():
    for p in PRODUCTOS:
        # 1. Buscamos o creamos la categoría primero
        cat, created = Categoria.objects.get_or_create(nombre=p['categoria'])
        
        # 2. Creamos el producto asociado a esa categoría
        # Usamos update_or_create por si vuelves a correr el script, 
        # así actualiza los datos en lugar de duplicar el producto.
        obj, created_prod = Producto.objects.update_or_create(
            nombre=p['nombre'],
            defaults={
                'categoria': cat,
                'precio': p['precio'],
                'precio_antes': p['precio_antes'],
                'descripcion': p['descripcion'],
                'imagen_url': p['imagen'],
                'stock': 10 # Les damos un stock inicial por defecto
            }
        )
        
        status = "Creado" if created_prod else "Actualizado"
        print(f"Producto: {p['nombre']} -> {status}")

if __name__ == "__main__":
    cargar_data()