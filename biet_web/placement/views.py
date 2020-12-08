from django.shortcuts import render
from .models import staff, infrastructure, infrastructure_gallery, contact, placement_updates
from .models import placement_glimpses, pre_placement_glimpses, hiring_statistics
from .models import Slider_Image, training_glimpses, industrial_collabrations_and_mou

# Create your views here.

def training_program(request):
    slider_image_data = Slider_Image.objects.all().order_by('sno')
    training_images = training_glimpses.objects.all()
    
    content = {
        'slider_image_data' : slider_image_data,
        'training_images' : training_images,
    }
    
    return render(request,'placement/training_program.html',content)

def placementDepartment(request):
    coordinators_data = staff.objects.all().order_by('sno')
    facilities_gallery = infrastructure_gallery.objects.all()
    infrastructure_data = infrastructure.objects.all()
    hiring_images = hiring_statistics.objects.all().order_by('sno')
    contacts_data = contact.objects.all().order_by('sno')
    placement_images = placement_glimpses.objects.all()
    pre_placement_images = pre_placement_glimpses.objects.all()
    slider_image_data = Slider_Image.objects.all().order_by('sno')
    mou_data = industrial_collabrations_and_mou.objects.all().order_by('sno')
    placement_updates_data = placement_updates.objects.all().order_by('-start_date')

    content = {
        'coordinators_data' : coordinators_data,
        'facilities_gallery' : facilities_gallery,
        'infrastructure_data' : infrastructure_data,
	'hiring_images' : hiring_images,
        'contacts_data' : contacts_data,
        'placement_images' : placement_images,
        'pre_placement_images' : pre_placement_images,
	'slider_image_data' : slider_image_data,
        'mou_data' : mou_data,
        'placement_updates_data' : placement_updates_data
    }
    
    return render(request,'placement/placement_dept.html',content)

def placementUpdates(request):
    placement_updates_data=placement_updates.objects.all().order_by('-start_date')
        
    content = {
        'placement_updates_data' : placement_updates_data
    }
        
    return render(request, 'placement/placement_updates.html', content)
