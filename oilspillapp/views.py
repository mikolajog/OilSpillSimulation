from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello Zuza Śmiech, if you let Mikołaj be so lazy, you will never finish this project!")
