from django.contrib import admin

# Register your models here.

from .models import auction,category

admin.site.register(auction)
admin.site.register(category)