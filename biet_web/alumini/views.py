from django.shortcuts import render

from .models import contact, staff, president, secretary
from .models import treasurer, members, alumni_corner, Slider_Image
from department.models import electrical_and_electronics_dept_alumni, mechanical_dept_alumni
from department.models import civil_dept_alumni, electronics_and_communication_dept_alumni
from department.models import chemical_dept_alumni, electronics_and_instrumentation_dept_alumni
from department.models import computer_science_dept_alumni, information_science_dept_alumni
from department.models import textile_technology_dept_alumni, bio_technology_dept_alumni

# Create your views here.
def alumni_association(request):
    president_data = president.objects.all().order_by('sno')
    secretary_data = secretary.objects.all().order_by('sno')
    treasurer_data = treasurer.objects.all().order_by('sno')
    members_data = members.objects.all().order_by('sno')
    coordinators_data = staff.objects.all().order_by('sno')
    contacts_data = contact.objects.all().order_by('sno')
    alumni_corner_data = alumni_corner.objects.all().order_by('-start_date')
    cs_alumni_data = computer_science_dept_alumni.objects.all().order_by('sno')
    ee_alumni_data = electrical_and_electronics_dept_alumni.objects.all().order_by('sno')
    me_alumni_data = mechanical_dept_alumni.objects.all().order_by('sno')
    cv_alumni_data = civil_dept_alumni.objects.all().order_by('sno')
    ec_alumni_data = electronics_and_communication_dept_alumni.objects.all().order_by('sno')
    ch_alumni_data = chemical_dept_alumni.objects.all().order_by('sno')
    ei_alumni_data = electronics_and_instrumentation_dept_alumni.objects.all().order_by('sno')
    is_alumni_data = information_science_dept_alumni.objects.all().order_by('sno')
    tx_alumni_data = textile_technology_dept_alumni.objects.all().order_by('sno')
    bt_alumni_data = bio_technology_dept_alumni.objects.all().order_by('sno')
    slider_image_data = Slider_Image.objects.all().order_by('sno')
    
    content={
        'slider_image_data' : slider_image_data,
        'alumni_corner_data': alumni_corner_data,
        'president_data': president_data,
        'secretary_data': secretary_data,
        'treasurer_data': treasurer_data,
        'members_data': members_data,
        'coordinators_data': coordinators_data,
        'cs_alumni_data': cs_alumni_data,
        'ee_alumni_data': ee_alumni_data,
        'me_alumni_data': me_alumni_data,
        'cv_alumni_data': cv_alumni_data,
        'ec_alumni_data': ec_alumni_data,
        'ch_alumni_data': ch_alumni_data,
        'ei_alumni_data': ei_alumni_data,
        'is_alumni_data': is_alumni_data,
        'tx_alumni_data': tx_alumni_data,
        'bt_alumni_data': bt_alumni_data, 
        'contacts_data': contacts_data,
    }
        
    return render(request,'alumini/alumni_association.html',content)

def alumni_corner_events(request):
    
    events=alumni_corner.objects.all().order_by('-start_date')
    content = {
        'events': events
    }
        
    return render(request, 'alumini/alumni_corner_events.html', content)
