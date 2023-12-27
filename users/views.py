from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden,HttpResponseBadRequest
# Create your views here.


def index(request):
    return render(request,'index.html')

def owner_register(request):
    return render(request,'owner_register.html')