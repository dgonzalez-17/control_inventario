from django.db import models


class Invoice(models.Model):
    name = models.CharField(max_length=100)
    numberInvoice = models.IntegerField()
    dateInvoice = models.DateField()
    documentNumber = models.IntegerField()
    amount = models.IntegerField()
    unitValue = models.IntegerField()
    discount = models.FloatField()
    total = models.FloatField()
    paidOut = models.FloatField()

def __str__(self):
    return self.name + " " + self.total + " " + self.paidOut 