from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    rarities = (
        ("Common",'Common'),
        ("Rare",'Rare'),
        ("Epic",'Epic'),
        ("Lengedary",'Legendary'),
        ('Unknown','Unknown')
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, name="name")
    amount = models.IntegerField(name="amount")
    rarity = models.CharField(name="rarity", choices=rarities, default='Unknown',max_length=10)
    power = models.IntegerField(name="power", max_length=3)
    description = models.TextField(name="description")
    date_added = models.DateTimeField(name='date_added',auto_now_add=True)