from django.db import models

# Create your models here.

class student(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    address = models.TextField(null=False, blank=False, max_length=200)
    image= models.ImageField()
    file =  models.FileField()

    def __str__(self):
        return self.name