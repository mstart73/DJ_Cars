from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Schedule, Typ_dict, Protocol

admin.site.register(Schedule)
admin.site.register(Typ_dict)
admin.site.register(Protocol)