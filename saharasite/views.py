from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormRegistrasi

def home(request):
    return render(request, 'saharasite/home.html', {})

def registrasi(request):

    form = FormRegistrasi()
    if request.method == 'POST':
        form = FormRegistrasi(request.POST)

    return render(request, 'saharasite/register.html', {'form':form})

