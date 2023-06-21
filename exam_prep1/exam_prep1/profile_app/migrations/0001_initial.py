# Generated by Django 4.2.2 on 2023-06-19 16:31

import django.core.validators
from django.db import migrations, models
import exam_prep1.profile_app.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)])),
                ('first_name', models.CharField(max_length=20, validators=[exam_prep1.profile_app.validators.profile_name_validator], verbose_name='First Name')),
                ('last_name', models.CharField(max_length=20, validators=[exam_prep1.profile_app.validators.profile_name_validator], verbose_name='Last Name')),
                ('profile_picture', models.URLField(blank=True, null=True, verbose_name='Profile Picture')),
            ],
        ),
    ]