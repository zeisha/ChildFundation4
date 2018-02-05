from django.db import models

from karbar.models import MyUser
from madadju.models import Madadju


class Admin(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    saving = models.IntegerField(default=0)


class AdminPayment(models.Model):
    date = models.DateField()
    value = models.IntegerField()
    receipt_number = models.IntegerField(default=0)
    madadju = models.ForeignKey(Madadju, on_delete=models.CASCADE)
    KIND_CHOICES = (
        ('ماهیانه', '1'),
        ('دفعه ای', '2'),
    )
    kind = models.CharField(max_length=10, choices=KIND_CHOICES, default='ماهیانه')


class Adapt2(models.Model):
    madadju=models.ForeignKey(Madadju, on_delete=models.CASCADE)
    admin=models.ForeignKey(Admin, on_delete=models.CASCADE)