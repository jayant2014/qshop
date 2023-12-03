# ecommerce_app/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', authentication.views.profile, name='profile'),
    path('products/', catalog.views.product_list, name='product_list'),
    path('cart/', cart.views.view_cart, name='view_cart'),
    path('checkout/', checkout.views.checkout, name='checkout'),
]
