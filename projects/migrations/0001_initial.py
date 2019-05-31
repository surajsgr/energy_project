# Generated by Django 2.1.3 on 2019-05-31 08:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='energy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Month', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('Day', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)])),
                ('Hour', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(24)])),
                ('Age_lt_5', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(58.16367)])),
                ('Age_range_5_to_18', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(151.225543)])),
                ('Age_range_18_to_25', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(581.636704)])),
                ('Age_range_25_to_65', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1163.273409)])),
                ('Age_gt_65', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(814.291386)])),
                ('Days_of_week', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)])),
                ('School_Day', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('Cloud_Cover_Fraction', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('Dew_point', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(-31.7), django.core.validators.MaxValueValidator(24.4)])),
                ('Humidity_Fraction', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0.18), django.core.validators.MaxValueValidator(1)])),
                ('Precipitable_Water', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(45)])),
                ('Temperature', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(-27), django.core.validators.MaxValueValidator(50)])),
                ('Visibility', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(34)])),
                ('Sector_FOOD_SERVICE', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('Sector_Grocery', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('Sector_K12_school', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('Sector_Lodging', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('Sector_office', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('Sector_residental', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('Sector_STAND_ALONE_RETAIL', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('Solar_Elevation', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
