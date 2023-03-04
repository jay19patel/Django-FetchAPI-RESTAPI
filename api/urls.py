from django.urls import path
from . import views


urlpatterns = [
    path('', views.API_Page, name="APIpage"),  
    path('addapi', views.addapi, name="addapi"),  
    path('getapi/<str:id>/', views.getapi, name="getapi"),  
    path('updateapi/<str:id>/', views.updateapi, name="updateapi"),  
    path('deleteapi/<str:id>/', views.deleteapi, name="deleteapi"),

   
]