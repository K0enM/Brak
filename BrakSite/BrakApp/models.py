from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Group(models.Model):
    Naam = models.CharField(max_length=35)

    def __str__(self):
        return self.Naam


class Groupmember(models.Model):
    Naam = models.CharField(max_length=20)
    Brakcounter = models.PositiveSmallIntegerField()
    Group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.Naam


class BRAK(models.Model):
    class BrakLevel(models.TextChoices):
        AMPER = 'AM', _('Amper')
        LICHTELIJK = 'LI', _('Lichtelijk')
        BEST_WEL = 'BW', _('Best wel')
        PITTIG = 'PI', _('Pittig')
        GESNEUVELD = 'SV', _('Gesneuveld')

    Datum = models.DateField(default=timezone.now)
    Brak_level = models.CharField(max_length=13, choices=BrakLevel.choices, default=BrakLevel.BEST_WEL)
    Groupmember = models.ForeignKey(Groupmember, on_delete=models.CASCADE)

    def __str__(self):
        return f"{str(self.Groupmember)} - {str(self.Datum)}"
