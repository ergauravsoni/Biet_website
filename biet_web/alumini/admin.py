from django.contrib import admin

from .models import contact, staff, president, secretary
from .models import treasurer, members, alumni_corner, Slider_Image

# Register your models here.
admin.site.register(Slider_Image)
admin.site.register(alumni_corner)
admin.site.register(president)
admin.site.register(secretary)
admin.site.register(treasurer)
admin.site.register(members)
admin.site.register(staff)
admin.site.register(contact)
