from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='items')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} {self.name}'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cart:cart', args=[str(self.id)])


