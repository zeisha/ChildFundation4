from django.db import models

from karbar.models import MyUser
from madadkar.models import Madadkar


class Madadju(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    physical_state = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=20)
    account = models.IntegerField()
    saving = models.IntegerField()
    GENDER_CHOICES = (
        ('مرد', 'Male'),
        ('زن', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='مرد')
    current_madadkar = models.ForeignKey(Madadkar, default=None, blank=True,
                                         null=True, on_delete=models.SET_NULL)


class Need(models.Model):
    madadju = models.ForeignKey(Madadju, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)


class UrgentNeed(models.Model):
    madadju = models.ForeignKey(Madadju, on_delete=models.CASCADE)
    need = models.CharField(max_length=500)


# class Letter(models.Model):
#     madadju = models.ForeignKey(Madadju, on_delete=models.CASCADE)
#     title = models.CharField(max_length=50)
#     content = models.CharField(max_length=1000)
#     date = models.DateField()
#     receiver_hamyar = models.ForeignKey('hamyar.Hamyar', on_delete=models.DO_NOTHING)


# To Admin
class Message(models.Model):
    madadju = models.ForeignKey(Madadju, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    date = models.DateField()


class Report(models.Model):
    madadju = models.ForeignKey(Madadju, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    date = models.DateField()