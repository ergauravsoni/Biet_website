from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Slider_Image(models.Model):
    sno = models.IntegerField()
    image = models.ImageField(upload_to='alumni/slider/')
    image_caption = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.sno) + " - " + self.image_caption[:80] + "..."
        
class alumni_corner(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    detail = models.FileField(upload_to = 'alumni/event/', blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True,blank=True)
    location = models.CharField(max_length=25)
    
    def __str__(self):
        return '{}'.format(self.title)

class president(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=300)
    
    def __str__(self):
        return str(self.sno) + ". " + str(self.name)
        
class secretary(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=300)
    
    def __str__(self):
        return str(self.sno) + ". " + str(self.name)
        
class treasurer(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=300)
    
    def __str__(self):
        return str(self.sno) + ". " + str(self.name)
        
class members(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=300)
    
    def __str__(self):
        return str(self.sno) + ". " + str(self.name)

class staff(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200,blank=True)
    department = models.CharField(max_length=200)
    image = models.ImageField(upload_to='alumni/staff/image/',blank=True)
    detail = models.FileField(upload_to='alumni/staff/data/',blank=True)
    email = models.EmailField(blank=True)
    sno = models.IntegerField(default='1')
    staff_type = models.CharField(max_length=100, choices=(
        ('DEAN', 'DEAN'),
        ('OTHER', 'OTHER'),), default='DEAN')
    description = models.TextField(blank=True,
     help_text='Enter description only for DEAN. For others this field can be skipped.')

    def __str__(self):
        return '{}'.format(self.name) + " : " + self.staff_type

class contact(models.Model):
    sno = models.IntegerField(default='1')
    name = models.CharField(max_length=200)
    alumni_designation = models.CharField(max_length=200)
    department_designation = models.CharField(max_length=200, blank=True)
    department = models.CharField(max_length=200,blank=True)
    email = models.EmailField(blank=True)
    contact_no = PhoneNumberField(blank=True)

    def __str__(self):
        return '{}'.format(self.name)

