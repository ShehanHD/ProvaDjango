from django.contrib import admin
from .models import services,about,team,event
# Register your models here.

admin.site.register(event)
admin.site.register(services)
admin.site.register(about)
admin.site.register(team)