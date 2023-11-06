# Generated by Django 4.2.7 on 2023-11-04 08:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("menu_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Menu",
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
                    "title",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Menu title"
                    ),
                ),
                ("url", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Название меню",
                "verbose_name_plural": "Названия меню",
            },
        ),
    ]
