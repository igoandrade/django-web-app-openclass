from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band

# Create your views here.
def hello(request):
    bands = Band.objects.all()
    return HttpResponse('<h1>Olá Django!</h1>')

def about(request):
    return HttpResponse('<h1>Sobre nós</h1><p>Somos uma loja online ...</p>')
