# Generated by Django 5.0 on 2024-01-30 00:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rango", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="likes",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="category",
            name="views",
            field=models.IntegerField(default=0),
        ),
    ]
