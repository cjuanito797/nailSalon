# Generated by Django 4.1 on 2022-09-21 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Scheduling", "0007_remove_timeslots_dayofweek_timeslots_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="technicianschedule", name="friday_timeSlots",
        ),
        migrations.RemoveField(
            model_name="technicianschedule", name="monday_timeSlots",
        ),
        migrations.RemoveField(
            model_name="technicianschedule", name="saturday_timeSlots",
        ),
        migrations.RemoveField(
            model_name="technicianschedule", name="sunday_timeSlots",
        ),
        migrations.RemoveField(
            model_name="technicianschedule", name="thursday_timeSlots",
        ),
        migrations.RemoveField(
            model_name="technicianschedule", name="tuesday_timeSlots",
        ),
        migrations.RemoveField(
            model_name="technicianschedule", name="wednesday_timeSlots",
        ),
    ]
