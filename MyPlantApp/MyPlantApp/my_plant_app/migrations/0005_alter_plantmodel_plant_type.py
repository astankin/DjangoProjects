# Generated by Django 4.2.1 on 2023-05-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_plant_app', '0004_alter_plantmodel_plant_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantmodel',
            name='plant_type',
            field=models.CharField(choices=[('Outdoor Plants', 'Outdoor Plants'), ('Indoor Plants', 'Indoor Plants')], max_length=14, verbose_name='Type:'),
        ),
    ]