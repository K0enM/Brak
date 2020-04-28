from django.db import models
from django.utils import timezone


# TODO Models hernoemen
# TODO Models veranderen inclusief data van BRAK

class Huis(models.Model):
    Naam = models.CharField(max_length=35)

    def __str__(self):
        return self.Naam


class Huisgenoot(models.Model):
    Naam = models.CharField(max_length=20)
    Brakcounter = models.PositiveSmallIntegerField()
    Huis = models.ForeignKey(Huis, on_delete=models.CASCADE)
    Laatst_brak = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Naam
