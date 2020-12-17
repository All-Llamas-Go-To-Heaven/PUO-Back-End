from django.db import models

# Create your models here.


class ProjectSubmission(models.Model):
    name = models.CharField(max_length=100)
    language_used = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    project_description = models.CharField(max_length=500)
    project_url = models.TextField(blank=True)
    project_photo = models.ImageField(upload_to='images/', default='images/default.jpg')
    portfolio_url = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    project = models.ForeignKey(ProjectSubmission, on_delete=models.CASCADE, related_name='posts')
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Endorse(models.Model):
    project = models.ForeignKey(ProjectSubmission, on_delete=models.CASCADE, related_name='endorsements')
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
