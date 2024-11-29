from django.db import models

# Create your models here.

class Device(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateField()
    image = models.ImageField(upload_to='media/')
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='devices',
    )
    features = models.ManyToManyField(
        'Feature',
        related_name='devices',
    )
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Feature(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title