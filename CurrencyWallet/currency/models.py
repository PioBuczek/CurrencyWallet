from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=20, decimal_places=6, null=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=20, decimal_places=8)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
