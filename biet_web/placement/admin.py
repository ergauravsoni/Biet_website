from django.contrib import admin
from .models import staff, infrastructure, infrastructure_gallery, contact, placement_updates
from .models import placement_glimpses, pre_placement_glimpses, hiring_statistics
from .models import Slider_Image, training_glimpses, industrial_collabrations_and_mou

# Register your models here.
admin.site.register(Slider_Image)
admin.site.register(placement_updates)
admin.site.register(staff)
admin.site.register(infrastructure)
admin.site.register(infrastructure_gallery)
admin.site.register(hiring_statistics)
admin.site.register(contact)
admin.site.register(placement_glimpses)
admin.site.register(pre_placement_glimpses)
admin.site.register(training_glimpses)
admin.site.register(industrial_collabrations_and_mou)
