from django.urls import path
from cobra_main import views

urlpatterns = [
    path('/index', views.index, name='index'),
]
