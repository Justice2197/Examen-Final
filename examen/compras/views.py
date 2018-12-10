from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import Productos, Tienda
from django.http import HttpResponse
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroForm, ProductosForm, TiendaForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
# Create your views here.
class InicioView(TemplateView):
    template_name = 'compras/inicio.html'

def index(request):
    return render(request, 'compras/inicio.html', {})

def base_layout(request):
	template='compras/inicio.html'
	return render(request,template)

def getdata(request):
	results=feed.objects.all()
	jsondata = serializers.serialize('json',results)
	return HttpResponse(jsondata)

class ProductosList(ListView):
    model = Productos

class ProductosView(DetailView):
    model = Productos

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/inicio")
    
class ProductosCreate(CreateView):
    model = Productos
    fields = ['nombre', 'costo_presupuesto', 'costo_real', 'tienda', 'notas']
    success_url = reverse_lazy('productos_list')

class ProductosUpdate(UpdateView):
    model = Productos
    fields = ['nombre', 'costo_presupuesto', 'costo_real', 'tienda', 'notas']
    success_url = reverse_lazy('productos_list')

class ProductosDelete(DeleteView):
    model = Productos
    success_url = reverse_lazy('productos_list')

class ProductosForm(ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'costo_presupuesto', 'costo_real', 'tienda', 'notas']

def productos_list(request, template_name='compras/productos_list.html'):
    productos = Productos.objects.all()
    data = {}
    data['object_list'] = productos
    return render(request, template_name, data)

def productos_view(request, pk, template_name='compras/productos_detail.html'):
    productos= get_object_or_404(Productos, pk=pk)    
    return render(request, template_name, {'object':productos})

def productos_create(request):
    if request.method == 'POST':
        form = ProductosForm(request.POST)
        
        if form.is_valid():

            producto = Productos(nombre = form.cleaned_data['nombre'],
                        costo_presupuesto = form.cleaned_data['costo_presupuesto'],
                        costo_real = form.cleaned_data['costo_real'],
                        tienda = form.cleaned_data['tienda'],
                        notas = form.cleaned_data['notas']
                        )

            producto.save()
            return redirect('inicio')

    else:

        form = ProductosForm()


    return render(request, 'compras/productos_form.html', {'form' : form})

def productos_update(request, pk, template_name='compras/productos_form.html'):
    productos= get_object_or_404(Productos, pk=pk)
    form = ProductosForm(request.POST or None, instance=productos)
    if form.is_valid():
        form.save()
        return redirect('producto_list')
    return render(request, template_name, {'form':form})

def productos_delete(request, pk, template_name='compras/productos_confirm_delete.html'):
    productos= get_object_or_404(Productos, pk=pk)    
    if request.method=='POST':
        productos.delete()
        return redirect('productos_list')
    return render(request, template_name, {'object':productos})

class TiendaList(ListView):
    model = Tienda

class TiendaView(DetailView):
    model = Tienda

def tienda_create(request):
    if request.method == 'POST':
        form = TiendaForm(request.POST)
        
        if form.is_valid():

            tienda = Tienda(nombre = form.cleaned_data['nombre'],
                        sucursal = form.cleaned_data['sucursal'],
                        direccion = form.cleaned_data['direccion'],
                        ciudad = form.cleaned_data['ciudad']
                        )

            tienda.save()
            return redirect('inicio')

    else:

        form = TiendaForm()


    return render(request, 'compras/tienda_form.html', {'form' : form})

class TiendaUpdate(UpdateView):
    model = Tienda
    fields = ['nombre', 'sucursal', 'direccion', 'ciudad', 'region']
    success_url = reverse_lazy('tienda_list')

class TiendaDelete(DeleteView):
    model = Tienda
    success_url = reverse_lazy('tienda_list')

class InfoView(TemplateView):
    template_name = 'compras/quienes_somos.html'

class ServicioView(TemplateView):
    template_name = 'compras/servicios.html'

class RegistroUsuario(CreateView):
    model = User
    template_name = 'compras/registro.html'
    form_class = RegistroForm
    success_url= reverse_lazy('productos_list')

class SignInView(LoginView):
    template_name = 'compras/login.html'

class SignOutView(LogoutView):
    pass
