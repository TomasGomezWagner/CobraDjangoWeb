from django.shortcuts import render
from django.http import HttpResponse

"""
def index(request):
    return HttpResponse('Hola mundo')
"""
def index(request):
    params = {}
    params['nombre_sitio'] = 'cobrachicken'
    return render(request, 'cobra_main/index.html', params)