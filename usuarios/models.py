from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import time

class DatoUsuaro(models.Model):
    usuario             = models.ForeignKey(User, on_delete=models.CASCADE,blank= True, null= True)
    imagen              = models.ImageField(upload_to='usuario/%Y/%m/%d', default='defecto/defecto.png', blank=True, null=True)
    nombre              = models.CharField(max_length=50)
    apellido            = models.CharField(max_length=50)
    fecha_nacimiento    = models.DateField(blank=True, null=True)
    pais                = models.CharField(max_length=30, blank=True)
    provincia           = models.CharField(max_length=40, blank=True)
    ciudad              = models.CharField(max_length=40, blank=True)
    domicilio           = models.CharField(max_length=80, blank=True)
    codogo_postal       = models.CharField(max_length=50, blank=True)
    telefono            = models.CharField(max_length=30, blank=True)
    celular             = models.CharField(max_length=30, blank=True)
    documento           = models.CharField(max_length=30, blank=True)
    cuit                = models.CharField(max_length=30, blank=True)
    
    def __str__(self) -> str:
        return self.usuario.username