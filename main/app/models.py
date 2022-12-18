from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=250)
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name
