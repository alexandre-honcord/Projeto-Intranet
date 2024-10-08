from django.db import models

class Tool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    links = models.TextField()
    image = models.ImageField(upload_to='default/tools/images/')
    target = models.TextField(default='#')
    def __str__(self):
        return self.name
    

class AppsTool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    links = models.TextField()
    image = models.ImageField(upload_to='default/AppTools/images/')
    target = models.TextField()

    def __str__(self):
        return self.name