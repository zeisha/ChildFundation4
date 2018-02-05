from django.db import models

from karbar.models import MyUser
from madadju.models import Madadju
from madadkar.models import Madadkar


class Hamyar(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    report_method = models.IntegerField(choices={(0, 'text'), (1, 'email')})

    def __str__(self):
        return str(self.user)


class Payment(models.Model):
    date = models.DateField()
    value = models.IntegerField()
    receipt_number = models.IntegerField(default=0)
    madadju = models.ForeignKey(Madadju, on_delete=models.CASCADE)
    hamyar = models.ForeignKey(Hamyar, on_delete=models.DO_NOTHING)
    KIND_CHOICES = (
        ('ماهیانه', '1'),
        ('دفعه ای', '2'),
    )
    kind = models.CharField(max_length=10, choices=KIND_CHOICES, default='ماهیانه')

class Gift(models.Model):
    date = models.DateField()
    madadju = models.ForeignKey(Madadju, on_delete=models.CASCADE)
    hamyar = models.ForeignKey(Hamyar, on_delete=models.DO_NOTHING)
    madadkar = models.ForeignKey(Madadkar, on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=3000)




class Adapt(models.Model):
    hamyar = models.ForeignKey(Hamyar, on_delete=models.CASCADE)
    madadju = models.ForeignKey(Madadju, on_delete=models.CASCADE)


class PaymentFoundation(models.Model):
    date = models.DateField()
    value = models.IntegerField()
    hamyar = models.ForeignKey(Hamyar, on_delete=models.DO_NOTHING)
    receipt_number = models.IntegerField(default=0)


