from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World")

def tapp(request):
    context ={'TEMPLATE_PATH':'TEMPLATE_PATH'}
    return render(request, "index.html",context)

