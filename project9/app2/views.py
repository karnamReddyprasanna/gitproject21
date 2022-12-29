from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def reddy(request):
    return HttpResponse('my name is prasanna')