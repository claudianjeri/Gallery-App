from django.shortcuts import render,redirect
from django.http import HttpResponse #this is returns a response to a user

# Create your views here.

def welcome(request):
    
    return HttpResponse('Gallery')

def search_results(request):
    pass

def image(request):
    pass

def filter_location(request):
    pass



