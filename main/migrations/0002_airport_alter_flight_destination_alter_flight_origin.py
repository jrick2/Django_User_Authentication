# Generated by Django 4.1 on 2022-08-10 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="airport",
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
                ("code", models.CharField(max_length=3)),
                ("city", models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name="flight",
            name="destination",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="arrival",
                to="main.airport",
            ),
        ),
        migrations.AlterField(
            model_name="flight",
            name="origin",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="departure",
                to="main.airport",
            ),
        ),
    ]