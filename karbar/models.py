from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    national_id = models.IntegerField(unique=True, blank=True)

    # address
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    postal_code = models.IntegerField()

    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    text = models.TextField(max_length=1000)
    sender = models.ForeignKey(MyUser, related_name='sender', on_delete=models.DO_NOTHING)
    receiver = models.ForeignKey(MyUser, related_name='receiver', on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'sender: ' + str(self.sender) + ' receiver: ' + str(self.receiver)
