from django.db import models

class KeyValue(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()

class Grain(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
