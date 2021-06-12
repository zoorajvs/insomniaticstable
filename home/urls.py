from django.urls import path

from home.views import Home

urlpatterns = [
    path('', Home ,name='home'),
]