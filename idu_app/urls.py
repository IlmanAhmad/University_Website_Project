from django.urls import path
from idu_app import views


app_name = 'idu'
urlpatterns = [
    path('', views.home, name='home'),
    path('studetails/', views.studetails, name='studetails'),
    path('registeration/', views.registeration, name='registeration'),
    path('marksheet/', views.marksheet, name='marksheet'),
    path('programmedetails/', views.programmedetails, name='programmedetails'),
    path('contact/', views.contactus, name='contact'),
    path('results/', views.results, name='results'),
    path('login/', views.handlelogin, name='login'),
    path('logout/', views.handlelogout, name='logout'),
   
]