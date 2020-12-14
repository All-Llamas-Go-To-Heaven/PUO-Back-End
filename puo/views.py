from django.shortcuts import render
from rest_framework import viewsets 
from .models import ProjectSubmission, Post, Endorse
from .serializers import ProjectSubmissionSerializer, PostSerializer, EndorseSerializer 

# Create your views here.
class ProjectSubmissionViewSet(viewsets.ModelViewSet):
    queryset = ProjectSubmission.objects.all()
    serializer_class = ProjectSubmissionSerializer
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class EndorseViewSet(viewsets.ModelViewSet):
    queryset = Endorse.objects.all()
    serializer_class = EndorseSerializer