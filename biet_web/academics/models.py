from django.db import models

# Create your models here.
class Library_User_Manual(models.Model):
    user_manual = models.FileField(upload_to = 'academics/library/user_manual/')

    def __str__(self):
        return '{}'.format(self.user_manual)

class Ranks(models.Model):
    year_range=models.CharField(max_length=9, help_text="Use this example format: 2019-2020")
    sno=models.IntegerField()
    uSN=models.CharField(max_length=10)
    name=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    rank=models.CharField(max_length=8, help_text="Use roman numerals for consistency. For example: I (for 1st rank)")
    course_type=models.CharField(max_length=2, choices=(('UG','UG'),('PG','PG'),))
    
    def __str__(self):
        return self.course_type + " : " + self.year_range + " : " + self.name
    

class Gallary(models.Model):
    image = models.ImageField(upload_to = 'academics/library/gallary/')

    def __str__(self):
        return '{}'.format(self.image)

class consultancyOrganizations(models.Model):
    
    sno=models.IntegerField()
    name_of_firms=models.CharField(max_length=250)
    
    def __str__(self):
        return str(self.sno) + ". " + str(self.name_of_firms[:80] + "...")
