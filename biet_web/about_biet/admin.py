from django.contrib import admin
from .models import Academic_Calender, Office_Staff, Deans, Governing_Body, Nain_Gallery
from .models import Governing_Council, Recognized_Research_Centres, Honors_And_Awards
from .models import Nain_Carousel, Research_Dean_Message, Funded_Projects_Department
from .models import Funded_Projects, kscst, Major_Events, Major_Events_Photos, Research_Advisory_Committee

# Register your models here.
admin.site.register(Academic_Calender)
admin.site.register(Office_Staff)
admin.site.register(Deans)
admin.site.register(Governing_Body)
admin.site.register(Governing_Council)
admin.site.register(Recognized_Research_Centres)
admin.site.register(Honors_And_Awards)
admin.site.register(Nain_Gallery)
admin.site.register(Nain_Carousel)
admin.site.register(Research_Dean_Message)
admin.site.register(Funded_Projects_Department)
admin.site.register(Funded_Projects)
admin.site.register(kscst)
admin.site.register(Major_Events)
admin.site.register(Major_Events_Photos)
admin.site.register(Research_Advisory_Committee)
