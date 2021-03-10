from django.db import models

import datetime

today = str(datetime.date.today())
cur_year = int(today[:4])

# Create your models here.
class UG_addmission(models.Model):
    addmission_fee = models.FileField(upload_to = 'addmission/UG/',blank=True)
    CourseWiseSeatMatrix = models.FileField(upload_to = 'addmission/UG/',blank=True)
    notification = models.FileField(upload_to = 'addmission/UG/',blank=True)
    application_form = models.FileField(upload_to = 'addmission/UG/',blank=True)
    cut_off = models.FileField(upload_to = 'addmission/UG/',blank=True)
    diploma_fee = models.FileField(upload_to = 'addmission/UG/',blank=True)

    def __str__(self):
        return '{}{}{}{}{}{}'.format(self.addmission_fee,self.CourseWiseSeatMatrix,self.notification,self.application_form,self.cut_off,self.diploma_fee)

class PG_addmission(models.Model):
    addmission_fee = models.FileField(upload_to = 'addmission/PG/',blank=True)
    CourseWiseSeatMatrix = models.FileField(upload_to = 'addmission/PG/',blank=True)
    notification = models.FileField(upload_to = 'addmission/PG/', default='coming-soon.png',blank=True)
    application_form = models.FileField(upload_to = 'addmission/PG/',blank=True)
    cut_off = models.FileField(upload_to = 'addmission/PG/', default='coming-soon.png',blank=True)

    def __str__(self):
        return '{}{}{}{}{}'.format(self.addmission_fee,self.CourseWiseSeatMatrix,self.notification,self.application_form,self.cut_off)

class Audit_Statement(models.Model):
    year_choices_array = []
    for year in range(2015, cur_year+1):
        year_choices_array.append((year, year))
    year_choices = tuple(year_choices_array)
    
    year = models.IntegerField(choices=year_choices)
    audit_statement = models.FileField(upload_to = 'addmission/Audit/')

    def __str__(self):
        return str(self.year) + ": " + '{}'.format(self.audit_statement)

class Prospectus(models.Model):
    prospectus = models.FileField(upload_to = 'addmission/Prospectus/')
    
    def __str__(self):
        return '{}'.format(self.prospectus)

