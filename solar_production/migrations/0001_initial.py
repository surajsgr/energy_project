# Generated by Django 2.1.3 on 2019-05-31 08:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='solar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Solar_Elevation', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(-68.228767), django.core.validators.MaxValueValidator(69.360406)])),
                ('Cloud_Cover_Fraction', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('Dew_Point', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(-27.2), django.core.validators.MaxValueValidator(40)])),
                ('Humidity_Fraction', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0.1445), django.core.validators.MaxValueValidator(1)])),
                ('Precipitation', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(41.1)])),
                ('Pressure', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(958.4), django.core.validators.MaxValueValidator(1011.2)])),
                ('Temperature', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(-23), django.core.validators.MaxValueValidator(50)])),
                ('Visibility', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(16.093)])),
                ('WindSpeed', models.FloatField(default='', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(18.5)])),
            ],
        ),
    ]
