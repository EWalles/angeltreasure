from xmlrpc.client import boolean
from django.db import models
from django.urls import reverse

# Create your models here
LOCATE = (
    ('N', 'Necklace'),
    ('R', 'Ring'),
    ('B', 'Bracelet'),
    ('E', 'Earring'),)

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

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('detail', kwargs={'jewelry_id': self.id})

class Customer(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=100)



class Set(models.Model):
    
    locate = models.CharField(
        max_length=1,
        choices=LOCATE,
        default=LOCATE[0][0]
    )


    jewelry = models.ForeignKey(Jewelry, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

