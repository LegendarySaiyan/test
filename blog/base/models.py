from django.db import models


class Data(models.Model):
    name = models.CharField(max_length = 255)
    uid = models.CharField(max_length = 255)
    balance = models.CharField(max_length = 255)
    hold = models.CharField(max_length = 255)
    status = models.BooleanField()

    def __str__(self):
        return self.name


