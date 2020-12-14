from rest_framework import serializers
from .models import ProjectSubmission, Post, Endorse

class PostSerializer(serializers.ModelSerializer):
    project_name = serializers.ReadOnlyField(source='project.name', read_only=True)
   

    class Meta:
        model = Post
        fields = ('name', 'comment', 'created_at', 'updated_at')

class EndorseSerializer(serializers.ModelSerializer):
    project_name = serializers.ReadOnlyField(source='project.name', read_only=True)

    class Meta:
        model = Endorse 
        fields = ('name', 'comment', 'created_at', 'updated_at')

class ProjectSubmissionSerializer(serializers.ModelSerializer):
    posts = PostSerializer(
        many=True,
        read_only=True
    )
    endorsements = EndorseSerializer(
        many=True,
        read_only=True
    )

    class Meta: 
        model = ProjectSubmission
        fields = ('name', 'project_name', 'project_description', 'project_url', 'project_photo', 'portfolio_url')
