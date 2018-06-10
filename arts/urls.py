from django.conf.urls import url #import thr url() 
from . import views #import view module
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[ #this is a list of url instances
    url('^$',views.home,name = 'home'), #url expression.
    url(r'^search/',views.search,name='search'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
