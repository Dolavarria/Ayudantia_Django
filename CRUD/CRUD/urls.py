from django.contrib import admin
from django.urls import path
from WEB import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.registrar_empleado, name='registrar_empleado'),
    path('listar/', views.listar_empleado, name='listar_empleado'),
    path('actualizar/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('eliminar/<int:id>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('registrar_departamento/', views.registrar_departamento, name='registrar_departamento'),  # Nueva ruta
    path('listar_departamento/', views.listar_departamento, name='listar_departamento'),  # Nueva ruta
]