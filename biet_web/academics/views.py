from django.shortcuts import render
from .models import Library_User_Manual, Ranks, Gallary
from placement.models import industrial_collabrations_and_mou

# Create your views here.

def library(request):
    return render(request,'academics/library.html')

def ranks(request):
    ranks_data=Ranks.objects.all().order_by('sno')
    setyr=set()
    setct=set()
    for record in ranks_data:
        setyr.add(record.year_range)
        setct.add(record.course_type)
    return render(request,'academics/ranks.html',{'ranks_data':ranks_data, 'setyr':sorted(setyr, reverse=True), 'setct':sorted(setct, reverse=True)})

def layout(request):
    return render(request,'academics/library/layout.html')

def staff(request):
    return render(request,'academics/library/staff.html')

def resources(request):
    return render(request,'academics/library/resources.html')

def membership(request):
    return render(request,'academics/library/membership.html')

def rules(request):
    return render(request,'academics/library/rules.html')
    
def biet_rules(request):
    return render(request,'academics/rules.html')

def services(request):
    return render(request,'academics/library/services.html')

def e_resources(request):
    return render(request,'academics/library/e_resources.html')

def committee(request):
    return render(request,'academics/library/committee.html')

def question_papers(request):
    return render(request,'academics/library/question_papers.html')

def online_courses(request):
    return render(request,'academics/library/online_courses.html')

def gallery(request):
    images = Gallary.objects.all()
    return render(request,'academics/library/gallery.html', {'images' : images})

def user_manual(request):
    user_manual = Library_User_Manual.objects.all()
    return render(request,'academics/library/user_manual.html',{'user_manual' : user_manual})

def perography(request):
    return render(request,'academics/library/perography.html')

def industry_collab(request):
    mou_data = industrial_collabrations_and_mou.objects.all().order_by('sno')
    content={'mou_data':mou_data}
    
    return render(request,'academics/industry_collab.html',content)
