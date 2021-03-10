from django.shortcuts import render
from .models import UG_addmission, PG_addmission, Audit_Statement, Prospectus

# Create your views here.
def ug_addmission(request):
    addmissions = UG_addmission.objects.all()
    return render(request,'admission/ug_addmission.html', {'addmissions' : addmissions})

def pg_addmission(request):
    addmissions = PG_addmission.objects.all()
    return render(request,'admission/pg_addmission.html', {'addmissions' : addmissions})

def contact(request):
    return render(request,'admission/contact.html')

def prospectus(request):
    prospectus_data = Prospectus.objects.all()
    
    content={'prospectus_data':prospectus_data}
    return render(request,'admission/prospectus.html',content)
    
def fee_structure(request):
    ug_addmissions = UG_addmission.objects.all()
    pg_addmissions = PG_addmission.objects.all()
    content = {'ug_addmissions' : ug_addmissions,'pg_addmissions' : pg_addmissions}
    return render(request,'admission/fee_structure.html',content)
    
def audit_statement(request):
    audit_data = Audit_Statement.objects.all().order_by('-year')
    
    content={'audit_data':audit_data}
    return render(request,'admission/audit_statement.html',content)

