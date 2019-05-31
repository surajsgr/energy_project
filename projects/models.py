from django.db import models

from django.core.validators import MinValueValidator,MaxValueValidator

class energy(models.Model):
    Month=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(12)])
    Day=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(31)])
    Hour=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(24)])
    Age_lt_5=models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(58.163670)])
    Age_range_5_to_18=models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(151.225543)])
    Age_range_18_to_25 = models.FloatField( validators=[MinValueValidator(0), MaxValueValidator(581.636704)])
    Age_range_25_to_65 = models.FloatField( validators=[MinValueValidator(0), MaxValueValidator(1163.273409)])
    Age_gt_65 = models.FloatField( validators=[MinValueValidator(0), MaxValueValidator(814.291386)])
    Days_of_week=models.FloatField( validators=[MinValueValidator(1), MaxValueValidator(7)])
    School_Day=models.FloatField( validators=[MinValueValidator(0), MaxValueValidator(1)])
    Cloud_Cover_Fraction=models.FloatField( validators=[MinValueValidator(0), MaxValueValidator(1)])
    Dew_point=models.FloatField( validators=[MinValueValidator(-31.70000), MaxValueValidator(24.4000)])
    Humidity_Fraction=models.FloatField( validators=[MinValueValidator(0.1800), MaxValueValidator(1)])
    Precipitable_Water=models.FloatField( validators=[MinValueValidator(3), MaxValueValidator(45)])
    Temperature = models.FloatField( validators=[MinValueValidator(-27), MaxValueValidator(50)])
    Visibility = models.FloatField( validators=[MinValueValidator(0), MaxValueValidator(34)])
    Sector_FOOD_SERVICE = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    Sector_Grocery=models.FloatField( validators=[MinValueValidator(0), MaxValueValidator(1)])
    Sector_K12_school=models.FloatField( validators=[MinValueValidator(0), MaxValueValidator(1)])
    Sector_Lodging=models.FloatField( validators=[MinValueValidator(0), MaxValueValidator(1)])
    Sector_office=models.FloatField( validators=[MinValueValidator(0), MaxValueValidator(1)])
    Sector_residental=models.FloatField( validators=[MinValueValidator(0), MaxValueValidator(1)])
    Sector_STAND_ALONE_RETAIL=models.FloatField( validators=[MinValueValidator(0), MaxValueValidator(1)])
    
class Project(models.Model):

    title = models.CharField(max_length=100)
    image = models.FilePathField(path="/static/energy")
