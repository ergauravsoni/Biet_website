from django.shortcuts import render
from .models import Graduation_Year, Graduation_Day, NAAC, Btech_Technowav
from .models import gymGallery, sacMembers, sacGallery, sac_Intro_Text

# Create your views here.
def naac(request):
    brochures = NAAC.objects.all()
    return render(request,'campus_life/naac.html',{'brochures' : brochures})

def nirf(request):
    return render(request,'campus_life/nirf.html')

def nain(request):
    return render(request,'campus_life/nain.html')

def green_campus(request):
    return render(request,'campus_life/green_campus.html')

def graduation_day(request):
    
    year = Graduation_Year.objects.all()
    image = Graduation_Day.objects.all()
    graduation_data = {'year': year, 'image': image}
    return render(request,'campus_life/graduation_day.html',graduation_data)

def to_be_updated(request):
    return render(request, 'to_be_updated.html')

def btech_technowav(request):
    btech_technowav_data = Btech_Technowav.objects.all()
    print(btech_technowav_data)
    return render(request, 'campus_life/btech_technowav.html',{'btech_technowav_data' : btech_technowav_data})

def gym(request):
    images = gymGallery.objects.all()
    return render(request,'campus_life/gym.html',{'images' : images})

def sac(request):
    intro_text = sac_Intro_Text.objects.all()
    sac_members = sacMembers.objects.all().order_by('sno')
    sac_images = sacGallery.objects.all().order_by('sno')
    content = {
	'intro_text': intro_text,
        'sac_members': sac_members,
        'sac_images': sac_images
    }
    return render(request,'campus_life/sac.html', content)
