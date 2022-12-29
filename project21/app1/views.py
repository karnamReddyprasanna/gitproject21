from django.shortcuts import render

# Create your views here.
def first(request):
    d={'name':'prasanna'}
    return render(request,'first.html',context=d)