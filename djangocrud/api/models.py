from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=256)
    year = models.IntegerField()


# Pertama Buat Model Dulu
class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    tlp = models.IntegerField()


class Supplier(models.Model):
    name_supplier = models.CharField(max_length=50)
    company = models.CharField(max_length=50)


class Inventory(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    id_supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE)
