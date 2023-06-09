from django.db import models
# Create your models here.
class Login(models.Model):
    name= models.CharField(max_length=255)
    password= models.CharField(max_length=255)
#   price=models.FloatField()
#   stock=models.IntegerField()
#   image=models.CharField(max_length=2550)


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    github = models.CharField(max_length=2550)