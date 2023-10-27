from django.db import models

# Create your models here.
class Car(models.Model):
    __tablename__ = 'car'
    id_car = models.IntegerField(primary_key=True)
    vin = models.CharField(max_length=17)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    color_code = models.CharField(max_length=20)
    park = models.CharField(max_length=50)
    visible = models.BooleanField(default=True)
    distans = models.IntegerField()
    current_reservation=models.IntegerField()
    warranty_date = models.DateTimeField()
    sell_date = models.DateTimeField()


class Client(models.Model):
    __tablename__ = 'client'
    id_client = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    adress_street = models.CharField(max_length=255)
    adress_nb = models.CharField(max_length=20)
    adress_postal = models.CharField(max_length=10)
    adress_city = models.CharField(max_length=255)

    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    person = models.CharField(max_length=255)
    agree = models.BooleanField(default=True)






