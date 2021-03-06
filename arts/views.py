from django.shortcuts import render,redirect
from django.http import HttpResponse #this is returns a response to a user
from .models import Image, Category, Location

# Create your views here.

def home(request):
    image = Image.get_images()
    category = Category.objects.all()
    return render(request,'index.html',{"image":image ,"categories":category})

def search(request):
        if 'category' in request.GET and request.GET["category"]:
            search_term = request.GET.get("category")
            searched_category = Image.search_by_category(search_term)
            

            return render(request,'search.html',{"messages":search_term,"categories":searched_category})

        else:
            message = "You haven't searched any category"
            return render(request,'search.html',{"message":message})

def image(request,image_id):
    try:
       image=Image.objects.get(id=image_id)
    except DoesNotExist:
       raise Http404()
    return render(request,'image.html',{"image":image})

def filter(request):
    image = Image.get_images()
    category = Category.objects.all()
    return render(request,'location.html',{"images":image ,"categories":category})




