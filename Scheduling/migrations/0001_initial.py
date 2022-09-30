# Generated by Django 4.1 on 2022-09-29 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TechnicianSchedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tech",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email"
                    ),
                ),
                ("monday_availability", models.BooleanField(default=False)),
                ("monday_timeIn", models.TimeField()),
                ("monday_timeOut", models.TimeField()),
                ("tuesday_availability", models.BooleanField(default=False)),
                ("tuesday_time_In", models.TimeField()),
                ("tuesday_time_Out", models.TimeField()),
                ("wednesday_availability", models.BooleanField(default=False)),
                ("wednesday_time_In", models.TimeField()),
                ("wednesday_time_Out", models.TimeField()),
                ("thursday_availability", models.BooleanField(default=False)),
                ("thursday_time_In", models.TimeField()),
                ("thursday_time_Out", models.TimeField()),
                ("friday_availability", models.BooleanField(default=False)),
                ("friday_time_In", models.TimeField()),
                ("friday_time_Out", models.TimeField()),
                ("saturday_availability", models.BooleanField(default=False)),
                ("saturday_time_In", models.TimeField()),
                ("saturday_time_Out", models.TimeField()),
                ("sunday_availability", models.BooleanField(default=False)),
                ("sunday_time_In", models.TimeField()),
                ("sunday_time_Out", models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name="timeSlots",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tech", models.EmailField(max_length=254, verbose_name="email")),
                ("date", models.DateField(blank=True)),
                ("nine_00_am", models.BooleanField(default=False)),
                ("nine_15am", models.BooleanField(default=False)),
                ("nine_30am", models.BooleanField(default=False)),
                ("nine_45am", models.BooleanField(default=False)),
                ("ten_00_am", models.BooleanField(default=False)),
                ("ten_15am", models.BooleanField(default=False)),
                ("ten_30am", models.BooleanField(default=False)),
                ("ten_45am", models.BooleanField(default=False)),
                ("eleven_00_am", models.BooleanField(default=False)),
                ("eleven_15am", models.BooleanField(default=False)),
                ("eleven_30am", models.BooleanField(default=False)),
                ("eleven_45am", models.BooleanField(default=False)),
                ("twelve_00_pm", models.BooleanField(default=False)),
                ("twelve_15pm", models.BooleanField(default=False)),
                ("twelve_30pm", models.BooleanField(default=False)),
                ("twelve_45pm", models.BooleanField(default=False)),
                ("one_00_pm", models.BooleanField(default=False)),
                ("one_15pm", models.BooleanField(default=False)),
                ("one_30pm", models.BooleanField(default=False)),
                ("one_45pm", models.BooleanField(default=False)),
                ("two_00_pm", models.BooleanField(default=False)),
                ("two_15pm", models.BooleanField(default=False)),
                ("two_30pm", models.BooleanField(default=False)),
                ("two_45pm", models.BooleanField(default=False)),
                ("three_00_pm", models.BooleanField(default=False)),
                ("three_15pm", models.BooleanField(default=False)),
                ("three_30pm", models.BooleanField(default=False)),
                ("three_45pm", models.BooleanField(default=False)),
                ("four_00_pm", models.BooleanField(default=False)),
                ("four_15pm", models.BooleanField(default=False)),
                ("four_30pm", models.BooleanField(default=False)),
                ("four_45pm", models.BooleanField(default=False)),
            ],
        ),
    ]
