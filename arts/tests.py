from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.

class CategoryTestClass(TestCase):
    #set up method
    def setUp(self):
        self.Potraits = Category(category_name="Potraits")

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Potraits,Category))

    def test_save_category(self):
        self.Potraits.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)    

    def test_delete_category(self):
        self.Potraits.save_category()
        self.Potraits.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)<1)
    

class LocationTestClass(TestCase):
    #set up method
    def setUp(self):
        self.Nairobi = Location(location="Nairobi")

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Nairobi,Location))

    def test_save_location(self):
        self.Nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_location(self):
        self.Nairobi.save_location()
        self.Nairobi.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)<1)

class ImageTestClass(TestCase):
    def setUp(self):

        self.Potrait = Image(name="Potrait",description="Tf am I supposed to say")
        self.Potrait.save()

        #creating new category and saving it
        self.Potraits = Category(category_name="Potraits")
        self.Potraits.save()

        #creating new location and saving it
        self.Nairobi = Location(location="Nairobi")
        self.Nairobi.save()

        self.Potrait.location.add(self.Nairobi)
        self.Potrait.category.add(self.Potraits)

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Potrait,Image))

    def test_save_image(self):
        self.Potrait.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)
    
    def test_delete_image(self):
        self.Potrait.save_image()
        self.Potrait.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)<1)