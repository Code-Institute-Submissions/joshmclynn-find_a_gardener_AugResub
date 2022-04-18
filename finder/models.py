from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField


# Create your models here.

# Model for business users
CHOICES = [('customer','Customer'),('business','Business')]
NEEDS = [('garden-maintenance','Garden-Maintenance'),('garden-design','Garden-Design'),('landscaping','Landscaping'),('tree-surgery','Tree-Surgery')]



class CustomUser(AbstractUser):
    user_type = MultiSelectField(choices = CHOICES, max_choices = 1)
    needs = MultiSelectField(choices = NEEDS, max_choices = 4)
    location = models.CharField(max_length=255, blank = True, editable=True)
    
    

    
    
   
        
                             
    
    