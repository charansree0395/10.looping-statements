from django.shortcuts import render

# Create your views here.

def loop(request):
    d={'name':'buddi'}
    return render(request,'for loop.html',d)