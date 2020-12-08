from django.contrib import admin
from .models import Graduation_Year, Graduation_Day, NAAC, Btech_Technowav
from .models import gymGallery, sacMembers, sacGallery, sac_Intro_Text

# Register your models here.
admin.site.register(Graduation_Year)
admin.site.register(Graduation_Day)
admin.site.register(NAAC)
admin.site.register(Btech_Technowav)
admin.site.register(gymGallery)
admin.site.register(sacMembers)
admin.site.register(sacGallery)
admin.site.register(sac_Intro_Text)
