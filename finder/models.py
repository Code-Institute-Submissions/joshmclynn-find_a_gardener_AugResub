from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

# Model for business users
class business(models.Model):
    company_name = models.CharField(max_length = 75, unique = True)
    f_name = models.CharField(max_length = 100)
    l_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 254, unique = True)
    image = CloudinaryField('image', default='placeholder')
    landscaping = models.BooleanField()
    maintenance = models.BooleanField()
    tree = models.BooleanField()
    design = models.BooleanField()
    date_joined = models.DateTimeField()
    location = models.CharField(max_length = 100)
    description = models.CharField(max_length = 300)


    

# Model for customer users
class customer(models.Model):
    f_name = models.CharField(max_length = 100)
    l_name = models.CharField(max_length = 100)
    image = CloudinaryField('image', default='placeholder')
    email = models.EmailField(max_length = 254, unique = True)
    landscaping = models.BooleanField()
    maintenance = models.BooleanField()
    tree = models.BooleanField()
    design = models.BooleanField()
    date_joined = models.DateTimeField()
    location = models.CharField(max_length = 100)

