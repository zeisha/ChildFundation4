from django.db import models

from karbar.models import MyUser
from madadju.models import Madadju


class Hamyar(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    report_method = models.IntegerField(choices={(0, 'text'), (1, 'email')})

    def __str__(self):
        return str(self.user)


class Payment(models.Model):
    date = models.DateField()
    value = models.IntegerField()
    madadju = models.ForeignKey(Madadju, on_delete=models.CASCADE)
    hamyar = models.ForeignKey(Hamyar, on_delete=models.DO_NOTHING)



class Adapt(models.Model):
    hamyar = models.ForeignKey(Hamyar, on_delete=models.CASCADE)
    madadju = models.ForeignKey(Madadju, on_delete=models.CASCADE)


class PaymentFoundation(models.Model):
    date = models.DateField()
    value = models.IntegerField()
    hamyar = models.ForeignKey(Hamyar, on_delete=models.DO_NOTHING)


