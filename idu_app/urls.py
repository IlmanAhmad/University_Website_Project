from django.urls import path
from idu_app import views


app_name = 'idu'
urlpatterns = [
    path('', views.home, name='home'),
    path('studetails/', views.studetails, name='studetails'),
   
]