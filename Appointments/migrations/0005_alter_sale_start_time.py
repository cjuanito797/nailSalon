# Generated by Django 4.1 on 2022-12-06 19:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointments', '0004_alter_sale_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='start_time',
            field=models.TimeField(blank=True, default=datetime.time(13, 35, 34, 20912), null=True),
        ),
    ]
