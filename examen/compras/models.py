from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Region(models.Model):
    nombre = models.CharField(max_length=40)


    def __str__(self):
        return self.nombre


class Ciudad(models.Model):
    nombre = models.CharField(max_length=20)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.nombre


class Tienda(models.Model):
    nombre = models.CharField(max_length=80)
    sucursal = models.CharField(max_length=80)
    direccion = models.CharField(max_length=80)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE,blank=True)

class Productos(models.Model):
    nombre = models.CharField(max_length=70)
    costo_presupuesto = models.IntegerField(blank=True)
    costo_real = models.IntegerField(blank=True)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE,blank=True)
    notas = models.TextField(max_length=200, blank=True)

def __str__(self):
        return self.name

def get_absolute_url(self):
        return reverse('productos_edit', kwargs={'pk': self.pk})
