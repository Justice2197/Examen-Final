from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.index),
     url('inicio', views.index, name='inicio'),
    path('', include('pwa.urls')),
    path(r'base_layout',views.base_layout,name='base_layout'),
    path('list_productos', views.ProductosList.as_view(), name='productos_list'),
    path('view/<int:pk>', views.ProductosView.as_view(), name='productos_view'),
    path('new_producto', views.productos_create, name='productos_new'),
    path('edit/<int:pk>', views.ProductosUpdate.as_view(), name='productos_edit'),
    path('delete/<int:pk>', views.ProductosDelete.as_view(), name='productos_delete'),
    path('list_tienda', views.TiendaList.as_view(), name='tienda_list'),
    path('view_tienda/<int:pk>', views.TiendaView.as_view(), name='tienda_view'),
    path('new_tienda', views.tienda_create, name='tienda_new'),
    path('edit_tienda/<int:pk>', views.TiendaUpdate.as_view(), name='tienda_edit'),
    path('delete_tienda/<int:pk>', views.TiendaDelete.as_view(), name='tienda_delete'),
]
