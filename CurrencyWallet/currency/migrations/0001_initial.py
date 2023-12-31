# Generated by Django 4.2 on 2023-09-02 18:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Crypto",
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
                ("name", models.CharField(max_length=255)),
                ("symbol", models.CharField(max_length=10)),
                ("price", models.DecimalField(decimal_places=6, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
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
                ("name", models.CharField(max_length=255)),
                ("type", models.CharField(max_length=255)),
                ("quantity", models.DecimalField(decimal_places=8, max_digits=20)),
                ("amount", models.DecimalField(decimal_places=8, max_digits=20)),
            ],
        ),
    ]
