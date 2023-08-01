from django.db import models

# Create your models here.

class Finch(models.Model):
    species = models.CharField()
    scientific_name = models.CharField()
    habitat = models.CharField()
    status = models.CharField()

    def __str__(self):
        return self.species