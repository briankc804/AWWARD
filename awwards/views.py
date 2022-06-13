from django.shortcuts import render
from django.http import JsonResponse
import datetime as dt

from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import ProfileSerializer, ProjectsSerializer
from . models import Profile, Projects
from awwards import serializers
from rest_framework import status

# Create your views here.
def welcome(request):
    date = dt.date.today()
    return render (request, 'drive.html',{"date": date})

def projects(request):
    post = Projects.objects.all()
    return render (request, 'drive.html',{"posts": post})



#Create a function that will Get all the profileList
            
# @api_view(['GET'])
# def profileList(request):
#     profiles = Profile.objects.all()
#     serializer = ProfileSerializer(profiles, many=True)
#     return Response(serializer.data)

#Create a class based views that will Get all the profileList

class profileList(APIView):
   def get(self, request, format=None):
       all_profiles = Profile.objects.all()
       serializer = ProfileSerializer(all_profiles, many=True)
       return Response(serializer.data)

class projectsList(APIView):
    
    def get(self, request, format=None):
        all_projects = Projects.objects.all()
        serializer = ProjectsSerializer(all_projects, many=True)
        
        return Response(serializer.data)
    
class projectsCreate(APIView):
    def post(self, request, format=None):
        serializer = ProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
            
            
            
   
   
   
   
   





