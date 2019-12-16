from django.db import models

# Create your models here.

class Url(models.Model):
    short_url = models.CharField(max_length=20)
    original_url = models.URLField("URL")
