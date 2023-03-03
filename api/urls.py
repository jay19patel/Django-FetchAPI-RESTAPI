from django.urls import path
from . import views


urlpatterns = [
    path('', views.API_Page, name="APIpage"),  
    path('addapi', views.addapi, name="addapi"),  
   
]