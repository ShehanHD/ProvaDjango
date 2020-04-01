from django.contrib import admin
from .models import quotes, event, book

# Register your models here.
admin.site.register(event)
admin.site.register(quotes)
admin.site.register(book)