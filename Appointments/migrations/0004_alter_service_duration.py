# Generated by Django 4.1 on 2022-09-07 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Appointments", "0003_alter_service_duration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="duration",
            field=models.DurationField(blank=True),
        ),
    ]

