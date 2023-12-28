from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone

# Create your models here.
class NewUser(AbstractUser):
    user_type = models.CharField(max_length=100, default='Tenant')
    contact_number = models.CharField(max_length=100,default='9876543210')
    address = models.CharField(max_length=800,default='abcd')
    landmark = models.CharField(max_length=600,default='xyz')
    city = models.CharField(max_length=500,default='hubli')
    state = models.CharField(max_length=300,default='Karnakata')
    country = models.CharField(max_length=400,default='India')
    status = models.BooleanField(default=0)

