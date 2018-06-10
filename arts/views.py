from django.shortcuts import render,redirect
from django.http import HttpResponse #this is returns a response to a user
from .models import Image

# Create your views here.

def home(request):
    image = Image.get_images()
    return render(request,'index.html',{"images":image})

def search(request):
        if 'category' in request.GET and request.GET["category"]:
            search_term = request.GET.get("category")
            searched_category = Image.search_by_category(search_term)
            # message = f"{search_term}"

            return render(request,'search.html',{"message":message,"categories":searched_category})

        else:
            message = "You havent searched any category"
            return render(request,'search.html',{"message":message})

def image(request,image_id):
    try:
       image=Image.objects.get(id=image_id)
    except DoesNotExist:
       raise Http404()
    return render(request,'image.html',{"image":image})


def filter_location(request):
    pass



