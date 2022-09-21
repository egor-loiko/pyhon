from django.db import models
# встроенная модель пользователя
# нужна для авторов сообщений
from django.contrib.auth.models import User
# тип "временнАя зона" для получения текущего времени
from django.utils import timezone


# Create your models here.
class Person(models.Model):
    person_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')


class Address(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)


class Message(models.Model):
    chat = models.ForeignKey(Person, verbose_name='Chat under person', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    message = models.TextField('Message')
    pub_date = models.DateTimeField('Message date', default=timezone.now)


class Mark(models.Model):
    person = models.ForeignKey(Person, verbose_name='Person', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    mark = models.IntegerField(verbose_name='Mark')
    pub_date = models.DateTimeField('Mark date', default=timezone.now)
