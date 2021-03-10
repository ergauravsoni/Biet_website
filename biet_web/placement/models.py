from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Slider_Image(models.Model):
    sno = models.IntegerField()
    image = models.ImageField(upload_to='placement/slider/')
    image_caption = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.sno) + " - " + self.image_caption[:80] + "..."

class placement_updates(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    detail = models.FileField(upload_to = 'placement/updates/', blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True,blank=True)
    location = models.CharField(max_length=25)
    
    def __str__(self):
        return '{}'.format(self.title)

class staff(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    image = models.ImageField(upload_to='placement/staff/image/',blank='True')
    detail = models.FileField(upload_to='placement/staff/data/',blank='True')
    sno = models.IntegerField(default='1')
    staff_type = models.CharField(max_length=100, choices=(
        ('DEAN', 'DEAN'),
        ('PB','PUBLIC RELATION'),
        ('OTHER', 'OTHER'),), default='DEAN')
    description = models.TextField(blank=True,
     help_text='Enter description only for DEAN. For others this field can be skipped.')

    def __str__(self):
        return '{}'.format(self.name) + " : " + self.staff_type
        
class infrastructure_gallery(models.Model):
    room_no = models.CharField(max_length=50, default='A321')
    image_type = models.CharField(max_length=100, choices=(
        ('PH', 'Placement Hall'),
        ('AUD','Auditorium'),
        ('PBR', 'Placement Board Room'),
        ('DR', 'Discussion Room'),
        ('LAB','Lab'),), default='PH')
    image = models.ImageField(upload_to='placement/infrastructure/gallery')

    def __str__(self):
        return '{}'.format(self.room_no) + " : " + self.image_type
        
class infrastructure(models.Model):
    facility_description = models.TextField()

    def __str__(self):
        return self.facility_description[:80] + "..."

class hiring_statistics(models.Model):
    sno = models.IntegerField()
    image = models.FileField(upload_to = 'placement/hiring_statistics/')

    def __str__(self):
        return '{}'.format(self.image)

class industrial_collabrations_and_mou(models.Model):
    sno = models.IntegerField()
    title_of_MOU = models.TextField()
    mOU_signed_with = models.TextField()
    signing_date = models.DateField(help_text="Use Format:YYYY-MM-DD or the calender button")
    
    def __str__(self):
        return self.title_of_MOU[:80] + "..."

class contact(models.Model):
    sno = models.IntegerField(default='1')
    name = models.CharField(max_length=200)
    training_and_placement_designation = models.CharField(max_length=200)
    department_designation = models.CharField(max_length=200, blank=True)
    department = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    contact_no = PhoneNumberField()

    def __str__(self):
        return '{}'.format(self.name)

class placement_glimpses(models.Model):
    image = models.FileField(upload_to = 'placement/placement_glimpses/')

    def __str__(self):
        return '{}'.format(self.image)
        
class pre_placement_glimpses(models.Model):
    image = models.FileField(upload_to = 'placement/pre_placement_glimpses/')

    def __str__(self):
        return '{}'.format(self.image)

class training_glimpses(models.Model):
    image = models.FileField(upload_to = 'placement/training_glimpses/')

    def __str__(self):
        return '{}'.format(self.image)

class students_placed_glimpses(models.Model):
    image = models.FileField(upload_to = 'placement/students_placed_glimpses/')

    def __str__(self):
        return '{}'.format(self.image)

class media_coverage(models.Model):
    image = models.FileField(upload_to = 'placement/media_coverage/')

    def __str__(self):
        return '{}'.format(self.image)
