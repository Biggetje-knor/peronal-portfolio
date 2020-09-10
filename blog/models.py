from django.db import models

class Blog(models.Model):
    titel = models.CharField(max_length= 100)
    omschrijving = models.CharField(max_length=1000)
    datum = models.DateField()

    def __str__(self):
        return self.titel

# Create your models here.
