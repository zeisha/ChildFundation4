from django.db import models

from karbar.models import MyUser


class Admin(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    saving = models.IntegerField(default=0)
