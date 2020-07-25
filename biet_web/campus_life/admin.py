from django.contrib import admin
from .models import Graduation_Year, Graduation_Day, NAAC, Btech_Technowav

# Register your models here.
admin.site.register(Graduation_Year)
admin.site.register(Graduation_Day)
admin.site.register(NAAC)
admin.site.register(Btech_Technowav)

