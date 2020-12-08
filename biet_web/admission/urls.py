from django.urls import path

from . import views

urlpatterns = [
    path('ug_addmission',views.ug_addmission, name='ug_addmission'),
    path('pg_addmission',views.pg_addmission, name='pg_addmission'),
    path('reserach',views.reserach, name='reserach'),
    path('admission/contact',views.contact, name='admission/contact'),
    path('admission/prospectus',views.prospectus, name='admission/prospectus'),
    path('admission/fee_structure',views.fee_structure, name='admission/fee_structure'),
    path('admission/career',views.career, name='admission/career'),
]
