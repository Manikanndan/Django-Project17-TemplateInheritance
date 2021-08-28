from django.shortcuts import render

# Create your views here.

def temInher_fun(request):
    return render(request,'TempInheritence.html')

def inheritance_fun(request):
    return render(request,'Inheritance.html')