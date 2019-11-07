from django.db import models
from django.utils import timezone

# Create your models here.
class Coffee(models.Model):
    name = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name


class Transaction(models.Model):
    time = models.DateTimeField(default=timezone.now)
    item = models.ForeignKey(Coffee, on_delete=models.PROTECT)
    pre_tax = models.FloatField()
    tax = models.FloatField()

    def __str__(self):
        return f"{self.item} at {self.time}"
