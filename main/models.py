from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    
    precio = models.DecimalField(max_digits=10, decimal_places=0) 
    precio_antes = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    
    descripcion = models.TextField()
    imagen_url = models.TextField(max_length=5000) 
    
    stock = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    @property
    def descuento_porcentaje(self):
        if self.precio_antes and self.precio_antes > self.precio:
            descuento = ((self.precio_antes - self.precio) / self.precio_antes) * 100
            return round(descuento)
        return 0

    def __str__(self):
        return self.nombre