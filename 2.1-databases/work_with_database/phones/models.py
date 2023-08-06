from django.db import models


class Phone(models.Model):
    name = models.TextField(max_length=50)
    price = models.TextField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()
    pass
