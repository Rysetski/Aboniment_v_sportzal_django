# Generated by Django 5.1.1 on 2025-01-27 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Discount",
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
                ("code", models.CharField(max_length=50, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("discount_percentage", models.FloatField()),
                ("valid_from", models.DateField()),
                ("valid_until", models.DateField()),
            ],
        ),
    ]
