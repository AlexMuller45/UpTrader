# Generated by Django 4.2.7 on 2023-11-04 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("menu_app", "0002_menu"),
    ]

    operations = [
        migrations.AddField(
            model_name="menuitem",
            name="menu",
            field=models.ForeignKey(
                blank=True,
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="menu_app.menu",
            ),
            preserve_default=False,
        ),
    ]
