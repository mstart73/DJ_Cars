# Generated by Django 4.2.6 on 2023-10-23 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0002_delete_schedule"),
    ]

    operations = [
        migrations.DeleteModel(name="Protocol",),
        migrations.DeleteModel(name="Typ_dict",),
    ]
