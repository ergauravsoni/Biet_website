from django.urls import path

from . import views

urlpatterns = [
    path('department/<str:course>/<str:dept>/home', views.home, name='home'),
    path('department/<str:course>/<str:dept>/events', views.events, name='events'),
]
