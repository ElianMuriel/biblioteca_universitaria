from django.db import models


class Libro(models.Model):
    isbn = models.CharField(max_length=20, unique=True)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    editorial = models.CharField(max_length=255)
    anio_publicacion = models.IntegerField()
    categoria = models.CharField(max_length=100)
    num_paginas = models.IntegerField()
    ubicacion = models.CharField(max_length=100, help_text="Ej: Estantería A3, Piso 2")
    estado = models.CharField(max_length=50, help_text="Ej: Disponible, Prestado, Dañado")
    copias_disponibles = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} ({self.isbn})"
