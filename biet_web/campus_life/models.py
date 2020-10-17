from django.db import models

import datetime;

today = str(datetime.date.today())
cur_year = int(today[:4])

class Graduation_Year(models.Model):
    year_choices_array = []
    for year in range(2015, cur_year+1):
        year_choices_array.append((year, year))
        year_choices = tuple(year_choices_array)
    year = models.IntegerField(choices=year_choices, primary_key=True)

    def __str__(self):
        return str(self.year)

# Create your models here.
class Graduation_Day(models.Model):
    year = models.ForeignKey(Graduation_Year, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'campus_life/graduation_day/image/')

    def __str__(self):
        return str(self.year) + ": " + str(self.image)

class NAAC(models.Model):
    brochure = models.FileField(upload_to = 'campus_life/NAAC/')

    def __str__(self):
        return '{}'.format(self.brochure)

class Btech_Technowav(models.Model):
    btech_technowav = models.FileField(upload_to = 'campus_life/btech_technowav/')
    type_id  = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.btech_technowav)

class gymGallery(models.Model):
    images = models.ImageField(upload_to='campus_life/gymGallery')

