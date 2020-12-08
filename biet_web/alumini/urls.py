from django.urls import path

from . import views

urlpatterns = [
    path('alumini/alumni_association',views.alumni_association, name='alumni_association'),
    path('alumini/alumni_corner_events',views.alumni_corner_events, name='alumni_corner_events'),
]
