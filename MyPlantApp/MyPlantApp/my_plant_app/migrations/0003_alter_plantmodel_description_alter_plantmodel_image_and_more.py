# Generated by Django 4.2.1 on 2023-05-19 12:33

import MyPlantApp.my_plant_app.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_plant_app', '0002_rename_plant_plantmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantmodel',
            name='description',
            field=models.TextField(verbose_name='Description:'),
        ),
        migrations.AlterField(
            model_name='plantmodel',
            name='image',
            field=models.URLField(verbose_name='Image Url:'),
        ),
        migrations.AlterField(
            model_name='plantmodel',
            name='name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), MyPlantApp.my_plant_app.validators.plant_name_validator], verbose_name='Name:'),
        ),
        migrations.AlterField(
            model_name='plantmodel',
            name='plant_type',
            field=models.CharField(choices=[('Outdoor Plants', 'Outdoor Plants'), ('Indoor Plants', 'Indoor Plants')], max_length=14, verbose_name='Type:'),
        ),
        migrations.AlterField(
            model_name='plantmodel',
            name='price',
            field=models.FloatField(verbose_name='Price:'),
        ),
    ]
