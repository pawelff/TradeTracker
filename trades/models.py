import datetime

from django.db import models


class Strategy(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Trade(models.Model):
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    profit = models.FloatField()
    currency = models.CharField(max_length=5)
    dolar_profit = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.strategy} profit: {self.profit}{self.currency}"
 