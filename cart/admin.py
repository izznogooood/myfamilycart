from django.contrib import admin

from .models import Item, Cart


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass
