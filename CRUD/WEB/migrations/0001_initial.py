# Generated by Django 5.0.6 on 2024-06-05 01:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Departamento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_departamento", models.CharField(max_length=200)),
                ("ubicacion", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Empleado",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_empleado", models.CharField(max_length=200)),
                ("apellido_empleado", models.CharField(max_length=100)),
                ("email_empleado", models.EmailField(max_length=50, unique=True)),
                ("edad_empleado", models.IntegerField()),
                (
                    "genero_empleado",
                    models.CharField(
                        choices=[
                            ("masculino", "Masculino"),
                            ("femenino", "Femenino"),
                            ("otro", "Otro"),
                        ],
                        max_length=80,
                    ),
                ),
                ("salario_empleado", models.IntegerField()),
                ("fecha_registro", models.DateTimeField(auto_now_add=True, null=True)),
                ("ultima_modificacion", models.DateTimeField(auto_now=True)),
                (
                    "departamento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="WEB.departamento",
                    ),
                ),
            ],
        ),
    ]
