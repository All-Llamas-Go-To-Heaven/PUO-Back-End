from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    password = models.TextField(max_length=10)
    school = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    portfolio_url = models.TextField(blank=True)
    location = models.CharField(max_length=100)
    my_story = models.CharField(max_length=1000)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
