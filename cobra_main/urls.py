from django.urls import path
from cobra_main import views

urlpatterns = [
    path('', views.index, name='index'), #si al principio le pongo algo es lo que se tiene que poner en la url despues de cobra_main
]
