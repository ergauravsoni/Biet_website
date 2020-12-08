from django.shortcuts import render
from .models import Sport, auditoriumGallary, sportsGallary, ewasteGallary
from .models import guestHouseGallary, drinkingWaterGallary, garbageGallary

# Create your views here.

def sport(request):
    report = Sport.objects.all().order_by('reports')
    sports_images = sportsGallary.objects.all()
    result = []

    for i in report:
        # print(i)
        reports_sports = {}
        reports_sports['url'] = str(i)
        reports_sports['title'] = str(i).split('/')[-1].split('.')[0]
        result.append(reports_sports)

    return render(request,'facilities/sport.html',{'result' : result, 'sports_images' : sports_images })

def hostel(request):
    return render(request,'facilities/hostel.html')

def canteen(request):
    return render(request,'facilities/canteen.html')

def scholarship(request):
    return render(request,'facilities/scholarship.html')

def dispensary(request):
    return render(request,'facilities/dispensary.html')

def perography(request):
    return render(request,'facilities/perography.html')

def internet(request):
    return render(request,'facilities/internet.html')

def transportation(request):
    return render(request,'facilities/transportation.html')

def elearning(request):
    return render(request,'facilities/elearning.html')

def language_lab(request):
    return render(request,'facilities/language_lab.html')
    
def ncc_nss(request):
    return render(request,'facilities/ncc_nss.html')

def ncc(request):
    return render(request,'facilities/ncc.html')
    
def nss(request):
    return render(request,'facilities/nss.html')
    
def redcross(request):
    return render(request, 'facilities/red_cross.html')

def ladies_rest_room(request):
    return render(request,'facilities/ladies_rest_room.html')

def auditorium(request):
    images = auditoriumGallary.objects.all()
    return render(request,'facilities/auditorium.html',{'images' : images})

def guest_house(request):
    images = guestHouseGallary.objects.all()
    return render(request,'facilities/guest_house.html',{'images' : images})
    
def drinking_water(request):
    images = drinkingWaterGallary.objects.all()
    return render(request,'facilities/drinking_water.html',{'images' : images})

def garbage(request):
    images = garbageGallary.objects.all()
    return render(request,'facilities/garbage.html',{'images' : images})

def ewaste(request):
    images = ewasteGallary.objects.all()
    return render(request,'facilities/ewaste.html',{'images' : images})

