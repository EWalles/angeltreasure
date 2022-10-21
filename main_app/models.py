from django.db import models
from django.urls import reverse

# Create your models here

class Bead(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

def get_absolute_url(self):
    return reverse('bead_detail', kwargs={'pk': self.id})

class Jewelry(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  beads = models.ManyToManyField(Bead)