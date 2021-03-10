from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Academic_Calender(models.Model):
    calender = models.FileField(upload_to = 'about_biet/calender/')

    def __str__(self):
        return '{}'.format(self.calender)

class Office_Staff(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='about_biet/office/image/')
    sno = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.name)

class Deans(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    responsibility = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    contact_no = PhoneNumberField()
    image = models.ImageField(upload_to='about_biet/deans/image/')
    description = models.TextField()
    detail = models.FileField(upload_to='about_biet/deans/data/')
    
    def __str__(self):
        return self.name + ": " + self.responsibility
        
class Governing_Body(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(default='',upload_to='about_biet/governing_body/image/')

    def __str__(self):
        return self.name + ": " + self.designation

class Governing_Council(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(default='',upload_to='about_biet/governing_council/image/')

    def __str__(self):
        return self.name + ": " + self.designation

class Research_Dean_Message(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    image = models.ImageField(upload_to='about_biet/research/image/')
    detail = models.FileField(upload_to='about_biet/research/data/',blank=True)
    description = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)

class Recognized_Research_Centres(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.sno) + ". " + self.name

class Funded_Projects_Department(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.sno) + ". " + str(self.name)
        
class Funded_Projects(models.Model):
    sno = models.IntegerField()
    title_of_project = models.TextField()
    funding_agency = models.CharField(max_length=400)
    amount_sanctioned = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    department = models.ForeignKey(Funded_Projects_Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.sno) + ". " + str(self.title_of_project[:80]) + "..."

class kscst(models.Model):
    kscst_pdf = models.FileField(upload_to = 'about_biet/research/')

    def __str__(self):
        return '{}'.format(self.kscst_pdf)

class Honors_And_Awards(models.Model):
    sno = models.IntegerField()
    faculty = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    name_of_the_award = models.CharField(max_length=500)
    awarded_by = models.CharField(max_length=500)
    awarded_on = models.CharField(max_length=100)
    awarded_for = models.TextField()
    
    def __str__(self):
        return str(self.sno) + ". " + self.faculty + ": " + self.name_of_the_award[:80] + "..."

class Nain_Carousel(models.Model):
    sno = models.IntegerField()
    images = models.ImageField(upload_to='about_biet/NAIN_Carousel')
    
    def __str__(self):
        return "Image " + str(self.sno)

class Nain_Gallery(models.Model):
    sno = models.IntegerField()
    images = models.ImageField(upload_to='about_biet/NAIN_Gallery')
    
    def __str__(self):
        return "Image " + str(self.sno)

class Major_Events(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=300)
    description = models.TextField()
    
    def __str__(self):
        return str(self.sno) + ". " + self.name
        
class Major_Events_Photos(models.Model):
    event = models.ForeignKey(Major_Events, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='about_biet/Major_Events')
    
    def __str__(self):
        return str(self.event.name) + ": " + '{}'.format(self.image)

class Research_Advisory_Committee(models.Model):
    sno = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=300)
    
    def __str__(self):
        return str(self.sno) + ". " + str(self.name)
