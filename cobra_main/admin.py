from django.contrib import admin
from cobra_main.models import Producto
from cobra_main.models import Diseño
from cobra_main.models import ProductoGenerado

class ProductoInLine(admin.TabularInline):
    
    model = ProductoGenerado
    extra = 0

@admin.register(Diseño)
class DiseñoAdmin(admin.ModelAdmin):
    #fields= ['nombre_imagen', 'ruta_imagen'] #orden en el que se ven los campos dentro de c/diseño
    fieldsets=[
        #("Relacion", {"fields":["categoria"]}),
        (
            "Datos generales",
            {
                "fields":[
                    'diseño', 'ruta_imagen', 'estado_diseño'
                ]
            },
        ),
    ]
    list_display= ['diseño', 'ruta_imagen', 'estado'] #columnas en la lista de diseños
    ordering = ['diseño'] #ordenamiento de la lista con - adelante va descendente ej '-nombre_imagen'
    list_filter = ('diseño', 'estado_diseño')
# admin.site.register(Diseño, DiseñoAdmin)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):

    fieldsets = [
        (
            "Datos generales",
            {
                "fields": [
                    'producto', 'precio', 'estado_producto'
                ]
            },
        ),
    ]
    list_display = ['producto', 'precio', 'estado']
    ordering = ['producto']
    list_filter = ('producto', 'estado_producto')
    inlines = [ProductoInLine]
    
# admin.site.register(Producto, ProductoAdmin)

@admin.register(ProductoGenerado)
class ProductoGeneradoAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Tipo de producto", {"fields":["producto"]}),
        (
            "Datos generales",
            {
                "fields": [
                    'diseño', 'estado_generado'
                ]
            },
        ),
    ]
    list_display = ['producto', 'diseño', 'precio', 'estado', 'upper_case_name']
    ordering = ['producto']
    list_filter = ('producto', 'diseño')

    @admin.display(description='Name') # para agregar columnas a las listas de productos
    def upper_case_name(self, obj):
        return ("%s %s" %(obj.producto, obj.estado_generado)).upper()
    
# admin.site.register(ProductoGenerado, ProductoGeneradoAdmin)