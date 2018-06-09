from django.conf.urls import url #import thr url() 
from . import views #import view module
from django.conf import settings

urlpatterns=[ #this is a list of url instances
    url('^home/$',views.home,name = 'home'), #url expression.
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    