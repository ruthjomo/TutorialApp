from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Models.
class  Project(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='project/', default='No image')
    title=models.CharField(max_length=60)
    description=models.TextField()
    link=models.CharField(max_length=100)
    location=models.CharField(max_length=30)
    posted=models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title
    
    def save_project(self):
        self.save()
    
    @classmethod    
    def get_project(cls, id):
        project=Project.objects.get(pk=id)
        return project

    @classmethod
    def search_project(cls, search_term):
        user = cls.objects.filter(title__icontains=search_term)
        return project 
    
    @classmethod   
    def delete_project(cls,delete_id):
        Project.objects.filter(pk=delete_id).delete()

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profile/', default='default.png')
    bio=models.TextField(blank=True)
    contact=models.CharField(max_length=30, blank=True)
    location=models.CharField(max_length=50,  blank=True)
    company=models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.user.username
    
    def save_profile(self):
        self.save()