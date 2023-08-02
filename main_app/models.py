from django.db import models
from django.urls import reverse

# Create your models here.

class Finch(models.Model):
    species = models.CharField()
    scientific_name = models.CharField()
    habitat = models.CharField()
    status = models.CharField()

    def __str__(self):
        return self.species
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})