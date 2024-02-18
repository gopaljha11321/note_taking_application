from  django.http import HttpResponse as hr;
from django.shortcuts import render;
def index(request):
    return hr("Note Taking Application")