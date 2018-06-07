from django.shortcuts import render
from django.http import HttpResponse #this is returns a response to a user

# Create your views here.

def welcome(request):
    title = 'Heeeeey'
    return render( title =title )

