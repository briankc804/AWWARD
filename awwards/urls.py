from django.urls import path
from . import views

urlpatterns = [
   path('', views.welcome, name='welcome'),
   path('projects/', views.projects, name='projects'),
   path('profile-list/',views.profileList.as_view() , name='profile-list'),
   path('projects-list/',views.projectsList.as_view() , name='projects-list'),
   path('projects-create/',views.projectsCreate.as_view() , name='projects-create'),
   
   #  path('create-user/', views.createUser, name='create-user'),
]
