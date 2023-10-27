# Generated by Django 4.2.6 on 2023-10-21 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                ("id_car", models.IntegerField(primary_key=True, serialize=False)),
                ("vin", models.CharField(max_length=17)),
                ("brand", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=255)),
                ("color_code", models.CharField(max_length=20)),
                ("park", models.CharField(max_length=50)),
                ("visible", models.BooleanField(default=True)),
                ("distans", models.IntegerField()),
                ("current_reservation", models.IntegerField()),
                ("warranty_date", models.DateTimeField()),
                ("sell_date", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                ("id_client", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("company", models.CharField(max_length=255)),
                ("adress_street", models.CharField(max_length=255)),
                ("adress_nb", models.CharField(max_length=20)),
                ("adress_postal", models.CharField(max_length=10)),
                ("adress_city", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=20)),
                ("person", models.CharField(max_length=255)),
                ("agree", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Protocol",
            fields=[
                (
                    "id_prot",
                    models.IntegerField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("id_rez", models.IntegerField()),
                ("date_rez_from", models.DateTimeField()),
                ("date_rez_to", models.DateTimeField()),
                ("model", models.CharField(max_length=255)),
                ("engine", models.CharField(max_length=255)),
                ("vin", models.CharField(max_length=17)),
                ("reg_number", models.CharField(max_length=30)),
                ("color", models.CharField(max_length=255)),
                ("company", models.CharField(max_length=255)),
                ("person", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=255)),
                ("adress", models.CharField(max_length=255)),
                ("nb_drive_licence", models.CharField(max_length=255)),
                ("pesel", models.IntegerField()),
                ("tel", models.CharField(max_length=255)),
                ("distans_release", models.IntegerField()),
                ("distans_return", models.IntegerField()),
                ("fuel_release", models.CharField(max_length=255)),
                ("fuel_return", models.CharField(max_length=255)),
                ("damage_release", models.CharField(max_length=1000)),
                ("damage_return", models.CharField(max_length=1000)),
                ("comment", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Schedule",
            fields=[
                (
                    "id_r",
                    models.IntegerField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("typ_r", models.IntegerField()),
                ("date1_r", models.DateTimeField()),
                ("date2_r", models.DateTimeField()),
                ("days_r", models.IntegerField()),
                ("id_car_r", models.IntegerField()),
                ("id_client_r", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Typ_dict",
            fields=[
                (
                    "id_typ",
                    models.IntegerField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("name_typ", models.CharField(max_length=100)),
                ("color", models.CharField(max_length=100)),
                ("name_color", models.CharField(max_length=200)),
            ],
        ),
    ]
