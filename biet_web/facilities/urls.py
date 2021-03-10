from django.urls import path

from . import views

urlpatterns = [
    path('facilities/sport',views.sport, name='sport'),
    path('facilities/auditorium',views.auditorium, name='auditorium'),
    path('facilities/guest_house',views.guest_house, name='guest_house'),
    path('facilities/drinking_water',views.drinking_water, name='drinking_water'),
    path('facilities/garbage',views.garbage, name='garbage'),
    path('facilities/ewaste',views.ewaste, name='ewaste'),
    path('facilities/boys_hostel',views.boys_hostel, name='boys_hostel'),
    path('facilities/ladies_hostel',views.ladies_hostel, name='ladies_hostel'),
    path('facilities/ladies_rest_room',views.ladies_rest_room, name='ladies_rest_room'),
    path('facilities/canteen',views.canteen, name='canteen'),
    path('facilities/scholarship',views.scholarship, name='scholarship'),
    path('facilities/dispensary',views.dispensary, name='dispensary'),
    path('facilities/perography',views.perography, name='perography'),
    path('facilities/internet',views.internet, name='internet'),
    path('facilities/transportation',views.transportation, name='transportation'),
    path('facilities/elearning',views.elearning, name='elearning'),
    path('facilities/language_lab',views.language_lab, name='language_lab'),
    path('facilities/ncc_nss',views.ncc_nss, name='ncc_nss'),
    path('facilities/ncc',views.ncc, name='ncc'),
    path('facilities/nss',views.nss, name='nss'),
    path('facilities/redcross',views.redcross, name='redcross'),
]

