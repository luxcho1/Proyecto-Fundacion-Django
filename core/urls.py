from django.urls import path
from .views import *


urlpatterns = [
    path('', root ),
    path('home', home, name='home'),
    path('info/', info, name='info'),  
    path('nosotros/', nosotros, name='nosotros'),  
    path('ubicacion/', ubicacion, name='ubicacion'),  
    path('contacto/', contacto, name='contacto'),  
]