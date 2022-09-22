import email
from lib2to3.pgen2 import token
from django.db import models
from hashlib import blake2s
from operator import mod, truediv
from pyexpat import model
from traceback import print_exc
from django import forms

# Create your models here.

class User(models.Model):
    email = models.EmailField(blank=True, null=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return self.username