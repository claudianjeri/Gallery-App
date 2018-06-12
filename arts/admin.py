from django.contrib import admin
from .models import Location, Category, Image


class ImageAdmin(admin.ModelAdmin): #This allows to customize the models inside the admin page.
    filter_horizontal =('category', 'location')#This(filter_horzontal) allows a certain ordering of many fields and pass in the category and location fields.

# Register your models here.
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image, ImageAdmin)