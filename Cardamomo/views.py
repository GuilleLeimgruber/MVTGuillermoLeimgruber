from django.http import HttpResponse
from django.shortcuts import render





def prueba_template(request):
    return render(request, 'prueba_template.html', context={})


def index(request):
    return render(request, 'index.html', context={})


def about(request):
    return render(request, 'about.html', context={})


