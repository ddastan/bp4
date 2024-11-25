from django.db import models

# Create your models here.

class Manas(models.Model):
    title = models.CharField(max_length=900)
    image = models.ImageField(upload_to='parser/image')
    genre = models.CharField(max_length=900)
    scheldule = models.CharField(max_length=500)
    def __str__(self):
        return self.title
