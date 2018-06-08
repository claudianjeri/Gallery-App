from django.shortcuts import render,redirect
from django.http import HttpResponse #this is returns a response to a user

# Create your views here.

def home(request):
    
    return render(request, 'index.html')



def image(request):
    pass

def filter_location(request):
    pass

def search_results(request):
    pass

