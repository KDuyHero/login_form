from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length=225)

    def __str__(self):
        return self.title

class User(AbstractUser):
    sex_choice = ((0,"Nu"), (1,"Nam"),(2,"Khong xax dinh"))
    age = models.IntegerField(default = 0)
    sex = models.ImageField(choices = sex_choice, default = 0)
    address = models.CharField(default ="", max_length = 100)