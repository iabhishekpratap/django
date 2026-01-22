from django.db import models

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
# __str__()  →  “How should this object look as a string?”
# Django needs to convert your object to text, it calls __str__().
