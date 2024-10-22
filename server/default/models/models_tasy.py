from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    IDtasy = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=50, null=True, blank=True)
    foto = models.ImageField(upload_to='default/users/photos/', null=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
