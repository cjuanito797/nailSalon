# Generated by Django 4.1 on 2022-11-16 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Appointments", "0012_remove_appointment_services"),
    ]

    operations = [
        migrations.RemoveField(model_name="sale", name="quantity",),
    ]
