from django.db import models

# Create your models here.


class ProjectSubmission(models.Model):
    name = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    project_description = models.CharField(max_length=500)
    project_url = models.TextField(blank=True)
    project_photo = models.ImageField(upload_to='media/images/', default='media/images/default.jpg')
    portfolio_url = models.TextField(blank=True)
