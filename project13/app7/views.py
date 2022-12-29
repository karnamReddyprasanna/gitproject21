from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
# Create your views here.
def second(request):
    return HttpResponse('<marquee><h1>by using views</h1></marquee>')
def third(request):
    return HttpResponse('<marquee><b>by using views</b></marquee>')