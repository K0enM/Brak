from django.contrib import admin

from .models import Huis, Huisgenoot, BRAK

# Register your models here.
admin.site.register(Huis)
admin.site.register(Huisgenoot)
admin.site.register(BRAK)
