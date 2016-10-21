from django.db import models

from goods.models import Good


class Cart(models.Model):
    session_id = models.IntegerField(unique=True)


class CartItem(models.Model):
    good = models.ForeignKey(Good)
    price = models.FloatField()
    qty = models.PositiveIntegerField()
    cart = models.ForeignKey(Cart)