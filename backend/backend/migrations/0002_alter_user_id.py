# Generated by Django 4.2.6 on 2023-10-19 00:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
