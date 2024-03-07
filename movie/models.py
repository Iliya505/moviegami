from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    summary = models.TextField()
    age = models.CharField(max_length=50)
    photo = models.ImageField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    published = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(unique=True)
    
    
    def __str__(self):
        return self.name

    class Meta:
        ordering=('name',)