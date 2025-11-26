from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=160, unique=True)
    isbn = models.PositiveIntegerField(max_length=13, null=False)
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    anio_publicacion = models.PositiveBigIntegerField(max_length=4)
    categoria = models.CharField(max_length=100)
    num_paginas = models.PositiveBigIntegerField(max_length=4)
    ubicacion = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    copias_disponibles = models.PositiveBigIntegerField(max_length=50)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return self.id
