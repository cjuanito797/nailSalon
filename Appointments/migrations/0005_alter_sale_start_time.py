# Generated by Django 4.1 on 2022-12-07 19:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointments', '0004_appointment_guest_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='start_time',
            field=models.TimeField(blank=True, default=datetime.time(13, 13, 57, 27417), null=True),
        ),
    ]
