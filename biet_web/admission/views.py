from django.shortcuts import render
from .models import UG_addmission, PG_addmission

# Create your views here.
def ug_addmission(request):
    addmissions = UG_addmission.objects.all()
    return render(request,'admission/ug_addmission.html', {'addmissions' : addmissions})

def pg_addmission(request):
    addmissions = PG_addmission.objects.all()
    return render(request,'admission/pg_addmission.html', {'addmissions' : addmissions})

def reserach(request):
    return render(request,'admission/research.html')

def contact(request):
    return render(request,'admission/contact.html')

def prospectus(request):
    return render(request,'admission/prospectus.html')
    
def fee_structure(request):
    ug_addmissions = UG_addmission.objects.all()
    pg_addmissions = PG_addmission.objects.all()
    content = {'ug_addmissions' : ug_addmissions,'pg_addmissions' : pg_addmissions}
    return render(request,'admission/fee_structure.html',content)
    
def career(request):
    return render(request,'admission/career.html')
