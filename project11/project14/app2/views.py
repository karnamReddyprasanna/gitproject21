from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('app2 first views')
def second(request):
    return HttpResponse('<h1>app2 second views</h1>')