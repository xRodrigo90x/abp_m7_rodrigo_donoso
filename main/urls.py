"""
URL configuration for tarea_m06 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from main import views


urlpatterns = [
    path('', views.index, name='index'),
    path('productos', views.productos, name='productos'),
    path('perfil', views.perfil, name='perfil'),
    path('servicios', views.servicios, name='servicios'),
    path('crear_usuario', views.crear_usuario, name='crear_usuario')
]
