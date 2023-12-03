# checkout/views.py
from django.shortcuts import render
from .models import Order

def checkout(request):
    order = Order.objects.create(user=request.user)
    return render(request, 'checkout/checkout.html', {'order': order})
