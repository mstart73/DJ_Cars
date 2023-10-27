from django.db import models

from cars.models import  Car
# Create your models here.


class Typ_dict(models.Model):
    __tablename__='typ_dict'
    id_typ=models.IntegerField(primary_key=True,auto_created=True)
    name_typ=models.CharField(null=False,max_length=100)
    color=models.CharField(null=False,max_length=100)
    name_color=models.CharField(max_length=200)

class Protocol(models.Model):
    __tablename__='protocol'
    id_prot=models.IntegerField(primary_key=True,auto_created=True)
    id_rez=models.IntegerField(null=False)
    date_rez_from=models.DateTimeField()
    date_rez_to = models.DateTimeField()
    model=models.CharField(max_length=255)
    engine=models.CharField(max_length=255)
    vin=models.CharField(max_length=17)
    reg_number=models.CharField(max_length=30)
    color=models.CharField(max_length=255)
    company=models.CharField(max_length=255)
    person=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    adress=models.CharField(max_length=255)
    nb_drive_licence=models.CharField(max_length=255)
    pesel=models.IntegerField()
    tel=models.CharField(max_length=255)
    distans_release=models.IntegerField()
    distans_return=models.IntegerField()
    fuel_release=models.CharField(max_length=255)
    fuel_return=models.CharField(max_length=255)
    damage_release=models.CharField(max_length=1000)
    damage_return=models.CharField(max_length=1000)
    comment = models.TextField()




class Schedule(models.Model):
    __tablename__ = 'schedule'
    id_r = models.IntegerField(primary_key=True,auto_created=True)
    Typ_dict = models.ForeignKey(Typ_dict,on_delete=models.CASCADE)

    date1_r = models.DateTimeField(null=False)
    date2_r = models.DateTimeField(null=False)
    days_r = models.IntegerField()
    car = models.ForeignKey(Car,on_delete=models.CASCADE)

    id_client_r = models.IntegerField()

    def __str__(self):
        return str(self.id_r)
