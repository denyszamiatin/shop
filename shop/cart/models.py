from django.db import models
from django import forms

from goods.models import Good


class Cart(models.Model):
    session_id = models.IntegerField(unique=True)


class CartItem(models.Model):
    good = models.ForeignKey(Good)
    price = models.FloatField()
    qty = models.PositiveIntegerField()
    cart = models.ForeignKey(Cart)


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ('qty',)