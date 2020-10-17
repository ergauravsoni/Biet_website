from django.contrib import admin
from .models import Event, News, Gallary, Video, Notification

# Register your models here.
admin.site.register(Event)
admin.site.register(News)
admin.site.register(Gallary)
admin.site.register(Video)
admin.site.register(Notification)
