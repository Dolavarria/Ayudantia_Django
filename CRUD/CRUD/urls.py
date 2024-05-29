"""
URL configuration for CRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from WEB import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.registrar_empleado, name='registrar_empleado'),
    path('listar/', views.listar_empleado, name='listar_empleado'),
    path('actualizar/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('eliminar/<int:id>/', views.eliminar_empleado, name='eliminar_empleado'),
]
