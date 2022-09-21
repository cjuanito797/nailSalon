# Generated by Django 4.1 on 2022-09-21 02:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("Scheduling", "0006_rename_twelve_15am_timeslots_twelve_15pm_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="timeslots", name="dayOfWeek",),
        migrations.AddField(
            model_name="timeslots",
            name="date",
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
