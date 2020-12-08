from django.db import models

# Create your models here.
class UG_addmission(models.Model):
    addmission_fee = models.FileField(upload_to = 'addmission/UG/',blank=True)
    CourseWiseSeatMatrix = models.FileField(upload_to = 'addmission/UG/',blank=True)
    notification = models.FileField(upload_to = 'addmission/UG/',blank=True)
    application_form = models.FileField(upload_to = 'addmission/UG/',blank=True)
    cut_off = models.FileField(upload_to = 'addmission/UG/',blank=True)

    def __str__(self):
        return '{}{}{}{}{}'.format(self.addmission_fee,self.CourseWiseSeatMatrix,self.notification,self.application_form,self.cut_off)

class PG_addmission(models.Model):
    CourseWiseSeatMatrix = models.FileField(upload_to = 'addmission/PG/',blank=True)
    notification = models.FileField(upload_to = 'addmission/PG/', default='coming-soon.png',blank=True)
    application_form = models.FileField(upload_to = 'addmission/PG/',blank=True)
    cut_off = models.FileField(upload_to = 'addmission/PG/', default='coming-soon.png',blank=True)

    def __str__(self):
        return '{}{}{}{}'.format(self.CourseWiseSeatMatrix,self.notification,self.application_form,self.cut_off)
