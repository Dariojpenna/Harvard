from distutils.command.upload import upload
from operator import mod, truediv
from pickle import TRUE
from typing_extensions import Self
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import AbstractUser
from django.db import models




#class MyModel(models.Model):
#    id = models.AutoField(primary_key=True)


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    pass

class category(models.Model):
    CategorieName=models.CharField(max_length=64)

    def __str__(self):
        return f'{self.CategorieName}'

class auction(models.Model):
    id = models.AutoField(primary_key=True)
    Article=models.CharField(max_length=64)
    Price=models.IntegerField()
    Description=models.TextField(max_length=500)
    Image=models.ImageField (upload_to='media', null=TRUE)
    Date=models.DateField(auto_now=True)
    Category=models.ForeignKey(category , on_delete=models.CASCADE, blank=True,null=True)
    Watchlist=models.ManyToManyField(User,blank=TRUE,null=TRUE,related_name='watchlist')

    def __str__(self):
        return f"{self.id}: {self.Article}   {self.Price} {self.Date} {self.Owner}"



class listings(models.Model):
    id = models.AutoField(primary_key=True)
    Article=models.CharField(max_length=64)
    LastOffert=models.IntegerField()
    Price=models.IntegerField()
    Image=models.ImageField()

    def __str__(self):
        return f"{self.id}: {self.Article} {self.LastOffert} {self.Price}"


class watchlist(models.Model):
    id = models.AutoField(primary_key=True)
    Article=models.CharField(max_length=64)
    Price=models.IntegerField()
    Description=models.TextField(max_length=500)
    Image=models.ImageField (upload_to='media', null=TRUE)
    
    
    
