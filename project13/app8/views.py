from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def four(request):
    return HttpResponse('<h2>my name is prasanna</h2>')
