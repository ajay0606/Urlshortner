from django.db import models

# Create your models here.

class Demo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title





        
