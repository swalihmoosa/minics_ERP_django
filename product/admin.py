from django.contrib import admin
from django.db import models

from product.models import ProductItem


class ProductItemadmin(admin.ModelAdmin):
    list_display = ["product_name", "product_price", "product_image"]

admin.site.register(ProductItem, ProductItemadmin)