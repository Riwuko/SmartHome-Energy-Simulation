# Generated by Django 3.2.13 on 2022-06-11 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarthome', '0009_alter_storagechargingandusageraport_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherraport',
            name='temperature',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weatherraport',
            name='wind_speed',
            field=models.FloatField(blank=True, null=True),
        ),
    ]