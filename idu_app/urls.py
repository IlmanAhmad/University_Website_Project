from django.urls import path
from idu_app import views


app_name = 'idu'
urlpatterns = [
    path('', views.home, name='home'),
    path('faculty/', views.faculty, name='faculty'),
    path('studetailsadmin/', views.studetailsadmin, name='studetailsadmin'),
    path('updatestudetailsadmin/', views.updatestudetailsadmin, name='updatestudetailsadmin'),
    path('sturegisterdetails/', views.sturegisterdetails, name='sturegisterdetails'),
    path('registeration/', views.registeration, name='registeration'),
    path('marksheet/', views.marksheet, name='marksheet'),
    path('updatemarksheet/', views.updatemarksheet, name='updatemarksheet'),
    path('programmedetails/', views.programmedetails, name='programmedetails'),
    path('contact/', views.contactus, name='contact'),
    path('results/', views.results, name='results'),
    path('login/', views.handlelogin, name='login'),
    path('logout/', views.handlelogout, name='logout'),
   
]