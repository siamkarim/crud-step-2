from django.db import models


# Create your models here.
class Student(models.Model):
    first_name =models.CharField( max_length=30)
    last_name = models.CharField( max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()

def __str__(self):
    return str(self.pk)+ " " + self.first_name+ " "+ self.last_name

