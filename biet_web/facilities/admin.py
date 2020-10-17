from django.contrib import admin
from .models import Sport, auditoriumGallary, sportsGallary, ewasteGallary
from .models import guestHouseGallary, drinkingWaterGallary, garbageGallary

# Register your models here.
admin.site.register(Sport)
admin.site.register(sportsGallary)
admin.site.register(auditoriumGallary)
admin.site.register(guestHouseGallary)
admin.site.register(drinkingWaterGallary)
admin.site.register(garbageGallary)
admin.site.register(ewasteGallary)

