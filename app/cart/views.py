# cart/views.py
from django.shortcuts import render
from .models import Cart

def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'cart/view_cart.html', {'cart': cart})
