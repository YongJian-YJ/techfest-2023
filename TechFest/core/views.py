from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

def product(request):
    return render(request, 'product.html')