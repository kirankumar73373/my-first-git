from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('this is my first view')

def balayya(request):
    return HttpResponse('Balayya is a such a sweetheart guy')

def ram(request):
    return HttpResponse('ram is a worst guy in the world')                     