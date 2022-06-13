from email.mime import image
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile (models.Model):
    bio = models.CharField(max_length=300)
    image = models.ImageField(default='project.jpg',upload_to='profile_images')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.bio
    
    def save_projects(self):
        self.save()
        
    def delete_projects(self):
        self.delete()
        
        
class Projects(models.Model):
    title = models.CharField(max_length=60)
    image = models.ImageField( default='project.jpg', upload_to='profile_images')
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    link = models.CharField(max_length=250)
    
    
    def __str__(self):
        return self.title
    
    def save_projects(self):
        self.save
        
    def delete_projects(self):
        self.delete

    
    
