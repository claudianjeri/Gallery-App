from django.conf.urls import url #import thr url() 
from . import views #import view module

urlpatterns=[ #this is a list of url instances
    url('^$', views.home, name = 'home'), #url expression.
   
]