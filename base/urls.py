from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add', add_to_cart, name='add_to_cart'),
    path('product/<int:id>', product, name='product'),
    path('cart', cart, name='cart'),
    path('shop', shop, name='shop'),
    path('product', product, name='product'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
