# Generated by Django 4.1 on 2022-12-06 22:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointments', '0002_alter_sale_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='start_time',
            field=models.TimeField(blank=True, default=datetime.time(16, 30, 46, 606591), null=True),
        ),
    ]
