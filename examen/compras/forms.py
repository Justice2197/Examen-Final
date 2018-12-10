from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
        ]
        labels = {
                'username': 'Nombre de usuario',
                'first_name': 'Nombre',
                'last_name': 'Apellidos',
                'email': 'Correo'
        }


            
class ProductosForm(forms.ModelForm):

 
    tienda = forms.ModelChoiceField(queryset=Tienda.objects.all(), empty_label="Seleccione una Tienda", label = "")

    class Meta:
        model = Productos

        fields = [
            'nombre', 
            'costo_presupuesto', 
            'costo_real', 
            'tienda', 
            'notas'
            ]

        labels = {
            'nombre': 'Nombre', 
            'costo_presupuesto': 'Costo Presupuestado', 
            'costo_real': 'Costro Real', 
            'tienda': 'Tienda', 
            'notas': 'Notas',
        }


class TiendaForm(forms.ModelForm):

    region = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label="Seleccione una Region", label = "")
    ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.all(), empty_label="Seleccione una Ciudad", label = "")

    class Meta:

        model = Tienda

        fields = (
            'nombre', 
            'sucursal', 
            'direccion', 
            'region',
            'ciudad'
        )

        labels = {
            'nombre': 'Nombre', 
            'sucursal': 'Sucursal', 
            'direccion': 'Direccion', 
            'region': 'Region',
            'ciudad': 'Ciudad', 
        }
