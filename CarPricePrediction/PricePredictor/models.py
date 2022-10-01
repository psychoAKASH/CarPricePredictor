from django.db import models


# Create your models here.
class Data(models.Model):
    data_id = models.AutoField(primary_key=True)
    year = models.IntegerField(default="")
    selling_price = models.FloatField(default="")
    kilometer_driven = models.FloatField(default="")
    fuel_type = models.IntegerField(default="")
    seller_type = models.IntegerField(default="")
    transmission = models.IntegerField(default="")
    owner = models.IntegerField(default="")

