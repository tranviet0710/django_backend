from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index1(request):
    return HttpResponse("Response to request index1 in polls2")