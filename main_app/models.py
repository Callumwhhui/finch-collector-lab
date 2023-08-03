from django.db import models
from django.urls import reverse


FED = (
    ('Y', 'Yes'),
    ('N', 'No')
)
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
    

class Feeding(models.Model):
    date = models.DateField('Date Fed')
    fed = models.CharField(
        max_length=1,
        choices=FED,
        default=FED[1][1]
        )
    
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_fed_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']