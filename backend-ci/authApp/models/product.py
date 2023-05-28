from django.db import models


class Product(models.Model):
    producto_id = models.AutoField(primary_key=True)
    nameProduto = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    precio_unitario = models.FloatField()
    talla = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
def __str__(self):
    return self.nameProduto + " " + self.marca