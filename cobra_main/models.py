from django.db import models
from django.utils.html import format_html

class Diseño(models.Model):

    Borrador = 'Borrador'
    Publicado = 'Publicado'
    Retirado = 'Retirado'
    APROBACION_DISEÑO = (
        (Borrador, 'Borrador'),
        (Publicado, 'Publicado'),
        (Retirado, 'Retirado'),
    )

    diseño = models.CharField(max_length=100)
    ruta_imagen = models.ImageField(upload_to = "diseño/%Y/%m/%d", blank= True, null= True)
    estado_diseño = models.CharField("Estado", max_length=20, choices=APROBACION_DISEÑO, default='Borrador')

    def estado(self):
        if self.estado_diseño == 'Borrador':
            return format_html('<span style="color: #146BFF;">{}</span>', self.estado_diseño)
        if self.estado_diseño == 'Publicado':
            return format_html('<span style="color: #0BDE35;">{}</span>', self.estado_diseño)
        if self.estado_diseño == 'Retirado':
            return format_html('<span style="color: #D91A09;">{}</span>', self.estado_diseño)

    def __str__(self) -> str:
        return self.diseño


class Producto(models.Model):

    Borrador = 'Borrador'
    Publicado = 'Publicado'
    Retirado = 'Retirado'
    APROBACION_PRODUCTO = (
        (Borrador, 'Borrador'),
        (Publicado, 'Publicado'),
        (Retirado, 'Retirado'),
    )

    producto = models.CharField(max_length=200)
    precio = models.FloatField(blank= True, null= True)
    estado_producto = models.CharField(max_length=20, choices=APROBACION_PRODUCTO, default='Borrador')

    def estado(self):
        if self.estado_producto == 'Borrador':
            return format_html('<span style="color: #146BFF;">{}</span>', self.estado_producto)
        if self.estado_producto == 'Publicado':
            return format_html('<span style="color: #0BDE35;">{}</span>', self.estado_producto)
        if self.estado_producto == 'Retirado':
            return format_html('<span style="color: #D91A09;">{}</span>', self.estado_producto)

    def __str__(self) -> str:
        return self.producto

class ProductoGenerado(models.Model):

    Generado = 'Generado'
    Pagado = 'Pagado'
    Enviado = 'Enviado'
    ESTADO_PRODUCTO_GENERADO = (
        (Generado, 'Generado'),
        (Pagado, 'Pagado'),
        (Enviado, 'Enviado'),
    )

    diseño = models.ForeignKey(Diseño, on_delete=models.CASCADE,blank= True, null= True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,blank= True, null= True)
    estado_generado = models.CharField("Estado",max_length=20, choices=ESTADO_PRODUCTO_GENERADO, default='Gereado')
    

    def estado(self):
        if self.estado_generado == 'Generado':
            return format_html('<span style="color: #146BFF;">{}</span>', self.estado_generado)
        if self.estado_generado == 'Pagado':
            return format_html('<span style="color: #0BDE35;">{}</span>', self.estado_generado)
        if self.estado_generado == 'Enviado':
            return format_html('<span style="color: #D91A09;">{}</span>', self.estado_generado)

    def precio(self):
        return self.producto.precio