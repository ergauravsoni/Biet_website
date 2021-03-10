from django.contrib import admin
from .models import UG_addmission, PG_addmission, Audit_Statement, Prospectus

# Register your models here.
admin.site.register(UG_addmission)
admin.site.register(PG_addmission)
admin.site.register(Audit_Statement)
admin.site.register(Prospectus)
