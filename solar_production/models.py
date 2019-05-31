from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
'''
Y = (1005.0092 * Solar Elevation) + ( -1.643e+04 * Cloud_Cover_Fraction) + (-1662.2771 * Dew_Point) + (-1.963e+04 * Humidity_Fraction) +
 ( -754.3373 *  Precipitation) + ( 47.0157 * Pressure) + (1044.2367 * Temperature) + (149.8066 * Visibility) + ( -156.0822 * Wind_Speed) 
'''

class solar(models.Model):


    Solar_Elevation=models.FloatField(validators=[MinValueValidator(-68.228767),MaxValueValidator(69.360406)])
    Cloud_Cover_Fraction=models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(1)])
    Dew_Point=models.FloatField(validators=[MinValueValidator(-27.20),MaxValueValidator(40)])
    Humidity_Fraction=models.FloatField(validators=[MinValueValidator(0.144500),MaxValueValidator(1)])
    Precipitation=models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(41.1)])
    Pressure=models.FloatField(validators=[MinValueValidator(958.400),MaxValueValidator(1011.200)])
    Temperature=models.FloatField(validators=[MinValueValidator(-23),MaxValueValidator(50)])
    Visibility=models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(16.0930)])
    WindSpeed=models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(18.500)])







# Create your models here.
