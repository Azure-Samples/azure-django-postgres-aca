# Generated by Django 3.1.7 on 2021-03-30 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cabin",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                ("description", models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name="Cruise",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("destination", models.CharField(max_length=50, unique=True)),
                ("description", models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name="CruiseCabin",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "cabin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="relecloud.cabin",
                    ),
                ),
                (
                    "cruise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="relecloud.cruise",
                    ),
                ),
            ],
        ),
    ]
