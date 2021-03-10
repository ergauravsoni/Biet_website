from django.shortcuts import render
from .models import Library_User_Manual, Ranks, Gallary, consultancyOrganizations
from placement.models import industrial_collabrations_and_mou

# Create your views here.

def library(request):
    return render(request,'academics/library.html',{'home':'active'})

def ranks(request):
    ranks_data=Ranks.objects.all().order_by('sno')
    setyr=set()
    setct=set()
    for record in ranks_data:
        setyr.add(record.year_range)
        setct.add(record.course_type)
    return render(request,'academics/ranks.html',{'ranks_data':ranks_data, 'setyr':sorted(setyr, reverse=True), 'setct':sorted(setct, reverse=True)})

def layout(request):
    return render(request,'academics/library/layout.html',{'layout':'active'})

def staff(request):
    return render(request,'academics/library/staff.html',{'staff':'active'})

def resources(request):
    return render(request,'academics/library/resources.html',{'resources':'active'})

def membership(request):
    return render(request,'academics/library/membership.html',{'membership':'active'})

def rules(request):
    return render(request,'academics/library/rules.html',{'rules':'active'})
    
def biet_rules(request):
    return render(request,'academics/rules.html')

def services(request):
    return render(request,'academics/library/services.html',{'services':'active'})

def e_resources(request):
    return render(request,'academics/library/e_resources.html',{'eresources':'active'})

def committee(request):
    return render(request,'academics/library/committee.html',{'committee':'active'})

def question_papers(request):
    return render(request,'academics/library/question_papers.html',{'qp':'active'})

def online_courses(request):
    return render(request,'academics/library/online_courses.html',{'courses':'active'})

def gallery(request):
    images = Gallary.objects.all()
    return render(request,'academics/library/gallery.html', {'images' : images, 'gallery':'active'})

def user_manual(request):
    user_manual = Library_User_Manual.objects.all()
    return render(request,'academics/library/user_manual.html',{'user_manual' : user_manual,'manual':'active'})

def perography(request):
    return render(request,'academics/library/perography.html',{'reprography':'active'})

def industry_collab(request):
    mou_data = industrial_collabrations_and_mou.objects.all().order_by('sno')
    content={'mou_data':mou_data}
    
    return render(request,'academics/industry_collab.html',content)

def consultancy(request):
    org_data = consultancyOrganizations.objects.all().order_by('sno')
    content={'org_data': org_data}
    
    return render(request,'academics/consultancy.html',content)
