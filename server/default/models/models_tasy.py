from django.db import models

class User(models.Model):
    IDtasy = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='default/users/photos/')
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
