from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255, name="name")
    amount = models.IntegerField(name="amount")
    rarity = models.IntegerField(name="rarity", default=0)
    power = models.FloatField(name="power", default=0)
    description = models.TextField(name="description")