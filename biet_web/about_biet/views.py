from django.shortcuts import render
from .models import Academic_Calender, Office_Staff, Deans, Governing_Body
from .models import Governing_Council, Recognized_Research_Centres
from placement.models import industrial_collabrations_and_mou

# Create your views here.
def Bapuji_educational_association(request):
    governing_council_data = Governing_Council.objects.all().order_by('sno')
    context = {'governing_council_data' : governing_council_data}
    return render(request,'about_biet/Bapuji_educational_association.html',context)

def Vision_Mission_Quality_Policies(request):
    return render(request,'about_biet/bietHome.html')

def academic_calender(request):
    academic_calender = Academic_Calender.objects.all()
    return render(request,'about_biet/academic_calender.html',{'academic_calender' : academic_calender})

def governing_body(request):
    governing_body_data = Governing_Body.objects.all().order_by('sno')
    return render(request,'about_biet/governing_body.html',{'governing_body_data' : governing_body_data})

def major_events(request):
    return render(request,'about_biet/major_events.html')

def nba(request):
    return render(request,'about_biet/nba.html')

def nain(request):
    return render(request,'about_biet/nain.html')

def naac(request):
    return render(request,'about_biet/naac.html')

def nirf(request):
    return render(request,'about_biet/nirf.html')

def director_msg(request):
    return render(request,'about_biet/director_msg.html')

def principal_msg(request):
    return render(request,'about_biet/principal_msg.html')

def chairman_msg(request):
    return render(request,'about_biet/chairman_msg.html')
    
def deans(request):
    deans_data = Deans.objects.all().order_by('sno')
    return render(request,'about_biet/deans.html',{'deans_data' : deans_data})

def office(request):
    office_member_data = Office_Staff.objects.all().order_by('sno')
    return render(request,'about_biet/office.html',{'office_member_data' : office_member_data})
    
def aicte(request):
    return render(request,'about_biet/aicte.html')

def research(request):
    return render(request,'about_biet/research.html')
    
def dean_message(request):
    return render(request,'about_biet/research/dean_message.html')
    
def recognized_research_centers(request):
    recog_research_data=Recognized_Research_Centres.objects.all().order_by('sno')

    return render(request,'about_biet/research/recognized_research_centers.html',{'recog_research_data':recog_research_data})    

def funded_projects(request):
    return render(request,'about_biet/research/funded_projects.html')
    
def kscst_projects(request):
    return render(request,'about_biet/research/kscst_projects.html')
    
def industry_collaboration(request):
    mou_data = industrial_collabrations_and_mou.objects.all().order_by('sno')
    content={'mou_data':mou_data}

    return render(request,'about_biet/research/industry_collaboration.html',content)
    
def product_development(request):
    return render(request,'about_biet/research/product_development.html')
    
def research_facilities(request):
    return render(request,'about_biet/research/research_facilities.html')
    
def honors_and_awards(request):
    return render(request,'about_biet/research/honors_and_awards.html')

def grievance_redressal(request):
    return render(request,'about_biet/other_committees/grievance_redressal.html')
    
def anti_ragging(request):
    return render(request,'about_biet/other_committees/anti_ragging.html')
    
def sc_st_obc_cell(request):
    return render(request,'about_biet/other_committees/sc_st_obc_cell.html')

def skill_cell(request):
    return render(request,'about_biet/other_committees/skill_development_cell.html')
    
def ipr_cell(request):
    return render(request,'about_biet/other_committees/ipr_cell.html')

def startup_cell(request):
    return render(request,'about_biet/other_committees/fablab.html')
    
def media_cell(request):
    return render(request,'about_biet/other_committees/media_cell.html')

def organisational_chart(request):
    return render(request,'about_biet/organisational_chart.html')
