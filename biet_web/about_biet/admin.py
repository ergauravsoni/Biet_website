from django.contrib import admin
from .models import Academic_Calender, Office_Staff, Deans, Governing_Body
from .models import Governing_Council, Recognized_Research_Centres

# Register your models here.
admin.site.register(Academic_Calender)
admin.site.register(Office_Staff)
admin.site.register(Deans)
admin.site.register(Governing_Body)
admin.site.register(Governing_Council)
admin.site.register(Recognized_Research_Centres)
