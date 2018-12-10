from django.contrib import admin
from .models import Productos, Tienda, Ciudad, Region
# Register your models here.
admin.site.register(Productos)
admin.site.register(Tienda)
admin.site.register(Ciudad)
admin.site.register(Region)