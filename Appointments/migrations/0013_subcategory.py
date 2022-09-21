# Generated by Django 4.1 on 2022-09-21 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Appointments", "0012_sale"),
    ]

    operations = [
        migrations.CreateModel(
            name="subCategory",
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
                ("name", models.CharField(db_index=True, max_length=200)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                (
                    "categorty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Appointments.category",
                    ),
                ),
            ],
        ),
    ]
