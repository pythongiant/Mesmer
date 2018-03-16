from django.db import models
from django.contrib.auth.models import User #Import the User module

class Profile(models.Model):
    Name = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255) 
    bio=models.TextField()
    DateOfBirth = models.DateField()
    profilePic  = models.FileField()
    def __str__(self):
        return self.Name.username+"("+self.username+")"
class Post(models.Model):
    post=models.TextField()
    image=models.FileField(blank=False)
    author = models.ForeignKey('Profile', on_delete=models.CASCADE)
