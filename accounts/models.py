from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class petOwner(models.Model):
    yourname = models.CharField(max_length=255, default='')
    ownerImage = models.ImageField(
        upload_to='Images/', default='Images/user_profile1.png', null=True)
    contact = models.CharField(max_length=13, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    email = models.EmailField()
    username = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.username


class petDoctor(models.Model):
    yourname = models.CharField(max_length=255, default='')
    doctorImage = models.ImageField(
        upload_to='Images/', default='Images/user_profile1.png', null=True)
    contact = models.CharField(max_length=13, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    email = models.EmailField()
    username = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.username
