from django.db import models

# Create your models here.
class Person(models.Model):
    person_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')


class Address(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
