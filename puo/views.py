from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import ProjectSubmission, Post, Endorse
from .serializers import ProjectSubmissionSerializer, PostSerializer, EndorseSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class ProjectSubmissionViewSet(viewsets.ModelViewSet):
    queryset = ProjectSubmission.objects.all()
    serializer_class = ProjectSubmissionSerializer
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class EndorseViewSet(viewsets.ModelViewSet):
    queryset = Endorse.objects.all()
    serializer_class = EndorseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


def perform_create(self, serializer):
    serializer.save(owner=self.request.user)
