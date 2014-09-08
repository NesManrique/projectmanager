from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def home(request):
    return render(request,'index.html')

def projectdet(request):
    return render(request,'project-detail.html')