# Generated by Django 4.1.7 on 2023-02-17 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0004_tablesea"),
    ]

    operations = [
        migrations.AlterField(
            model_name="station",
            name="uid_station",
            field=models.CharField(max_length=5),
        ),
    ]