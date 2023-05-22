# Generated by Django 4.2.1 on 2023-05-19 12:33

import MyPlantApp.authapp.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_rename_profile_profilemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='first_name',
            field=models.CharField(max_length=20, validators=[MyPlantApp.authapp.validators.user_name_validator], verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='last_name',
            field=models.CharField(max_length=20, validators=[MyPlantApp.authapp.validators.user_name_validator], verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='profile_picture',
            field=models.URLField(blank=True, null=True, verbose_name='Profile Picture'),
        ),
    ]