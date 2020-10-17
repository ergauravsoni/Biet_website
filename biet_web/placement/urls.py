from django.urls import path

from . import views

urlpatterns = [
    path('placement/training_program',views.training_program, name='training_program'),
    path('placement/placement_dept',views.placementDepartment, name='placementDepartment'),
]
