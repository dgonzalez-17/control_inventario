from django.db import models


class Logistic(models.Model):
    Logistics_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    documentType = models.CharField(max_length=100)
    documentNumber = models.IntegerField()
    mailAddress = models.EmailField()
    phone = models.IntegerField()
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    birthDate = models.DateField()
    nickName = models.CharField(max_length=50)
    password = models.CharField(max_length=32)

def __str__(self):
    return self.name + " " + self.lastName 