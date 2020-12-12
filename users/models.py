from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='email',max_length=255, unique=True)
    password = models.CharField(max_length=50, min_length=10)
    school = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    portfolio_url = models.TextField(blank=True)
    location = models.CharField(max_length=100)
    my_story = models.CharField(max_length=1000)

    REQUIRED_FIELDS = ['username', 'password']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.em
