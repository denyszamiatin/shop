from django.shortcuts import render

def add(request):
    return render(request, 'cart.html')
