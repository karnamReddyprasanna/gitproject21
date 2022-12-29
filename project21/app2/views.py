from django.shortcuts import render

# Create your views here.
def second(request):
    f={'name':'sudheep','age':5}
    return render(request,'h4.html',context=f)
