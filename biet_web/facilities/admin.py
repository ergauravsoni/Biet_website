from django.contrib import admin
from .models import Sport, auditoriumGallary, sportsGallary

# Register your models here.
admin.site.register(Sport)
admin.site.register(sportsGallary)
admin.site.register(auditoriumGallary)

