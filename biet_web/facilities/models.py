from django.db import models

# Create your models here.
class Sport(models.Model):
    reports = models.FileField(upload_to = 'facilities/Sport/')

    def __str__(self):
        return '{}'.format(self.reports)

class sportsGallary(models.Model):
    images = models.ImageField(upload_to='facilities/sportsGallary')
    
    def __str__(self):
        return str(self.images)

class auditoriumGallary(models.Model):
    images = models.ImageField(upload_to='facilities/auditoriumGallary')

class guestHouseGallary(models.Model):
    images = models.ImageField(upload_to='facilities/guestHouseGallary')

class drinkingWaterGallary(models.Model):
    images = models.ImageField(upload_to='facilities/drinkingWaterGallary')

class garbageGallary(models.Model):
    images = models.ImageField(upload_to='facilities/garbageGallary')

class ewasteGallary(models.Model):
    images = models.ImageField(upload_to='facilities/ewasteGallary')

