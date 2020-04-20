from django.db import models
from django.utils import timezone


class Huis(models.Model):
    naam = models.CharField(max_length=35)

    def __str__(self):
        return self.naam


class Huisgenoot(models.Model):
    naam = models.CharField(max_length=20)
    brakcounter = models.PositiveSmallIntegerField()
    huis = models.ForeignKey(Huis, on_delete=models.CASCADE)
    laatst_brak = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.naam
