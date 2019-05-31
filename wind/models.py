from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator


class Wind(models.Model):

    WindSpeed=models.FloatField(validators=[MinValueValidator(0.200),MaxValueValidator(30)])




# Create your models here.
