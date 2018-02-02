from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.name + ' : ' + self.title
