from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userProfile(models.Model):
    user=models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pic')
