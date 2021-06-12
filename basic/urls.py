from django.urls import path

from .views import About, Services, Contact , Terms , Contactsuccess

urlpatterns = [
    path('about/', About, name='about'),
    path('services/', Services, name='services'),
    path('contact/', Contact,name = 'contact'),
    path('contactsucess/',Contactsuccess ,name= 'contactsuccess'),
    path('termsofuse/',Terms , name='terms-of-use')

]
