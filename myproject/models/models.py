from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)             # small text
    bio = models.TextField()                            # long text
    age = models.IntegerField()                         # whole number
    percentage = models.FloatField()                    # decimal number
    birth_date = models.DateField()                     # only date
    email = models.EmailField(unique=True)              # email field

    def __str__(self):
        return self.name


