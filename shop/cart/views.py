from django.shortcuts import render, redirect
from .models import CartItem, CartItemForm


def add(request):
    return render(request, 'cart.html')


def view(request):
    cart_items = CartItem.objects.filter(cart__session_id=111)
    forms = [(item.pk, item.good.name, CartItemForm(instance=item)) for item in cart_items]
    return render(request, "cartview.html", {'forms': forms})


def change(request):
    ci = CartItem.objects.get(pk=int(request.POST['gid']))
    ci.qty = request.POST['qty']
    ci.save()
    return redirect('/cart/view')