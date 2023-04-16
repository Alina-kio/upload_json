from django.db import models

class MyModel(models.Model):
    symbol = models.CharField(max_length=100)
    price = models.CharField(max_length=100)