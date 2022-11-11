from django.db import models

class Nex(models.Model):
    nomi = models.CharField(max_length=20)
    tezligi = models.IntegerField(default=1)
    rangi = models.CharField(max_length=20)


def __str__(self):
    return f"{self.nomi} , {self.tezligi} , {self.rangi}"