# Generated by Django 4.2.6 on 2023-10-22 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(name="Schedule",),
    ]
