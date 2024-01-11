from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    categories=[
        (0,'Western'),
        (1,'Ethnic'),
        (2,'casual'),
    ]
    name = models.CharField(max_length=80)
    price = models.IntegerField(default=0)
    qty = models.SmallIntegerField(default=0)
    category=models.IntegerField(default=0,choices=categories)
    brand = models.CharField(max_length=30)
    description=models.TextField()
    image = models.URLField()

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    qty=models.IntegerField(default=1)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)

class Contact(models.Model):
    name=models.CharField(max_length=10)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    message=models.TextField()

class blog(models.Model):
    image= models.URLField()
    name=models.CharField(max_length=90)
    description=models.TextField()

class contactform(models.Model):
    email=models.EmailField()
    message=models.TextField()
 
class user_signup(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=25)
    con_password=models.CharField(max_length=25)
    def __str__(self):
        return self.name