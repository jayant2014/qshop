# checkout/models.py
from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Add more order fields as needed

    def __str__(self):
        return f"Order for {self.user.username}"
