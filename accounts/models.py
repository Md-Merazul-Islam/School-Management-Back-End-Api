from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    account_no  = models.IntegerField(unique=True)
    profile_image = models.ImageField(upload_to='account/images', blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.username} Profile : {self.account_no}'
