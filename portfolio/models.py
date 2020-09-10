from django.db import models

class Project(models.Model):
    titel = models.CharField(max_length=100)
    omschrijving = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)


    def __str__(self):
        return self.titel

# Create your models here.
