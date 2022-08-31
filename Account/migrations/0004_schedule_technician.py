# Generated by Django 4.1 on 2022-08-31 00:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("Account", "0003_technician_techschedule"),
    ]

    operations = [
        migrations.AddField(
            model_name="schedule",
            name="technician",
            field=models.EmailField(
                default=django.utils.timezone.now,
                max_length=254,
                unique=True,
                verbose_name="email",
            ),
            preserve_default=False,
        ),
    ]
