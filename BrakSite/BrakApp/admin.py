from django.contrib import admin

from .models import Group, Groupmember, BRAK

# Register your models here.
admin.site.register(Group)
admin.site.register(Groupmember)
admin.site.register(BRAK)
