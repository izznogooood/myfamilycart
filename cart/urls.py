from django.urls import path
from . import views as user_views

app_name = 'cart'

urlpatterns = [
    # JavaScript API Endpoints
    # path('api/items/<int:cart_id>', user_views.get_items, name='items-json'),
    # path('api/carts', user_views.get_carts, name='carts-json'),

    path('api/items/create', user_views.create_item, name='create-item'),
    path('api/carts/create', user_views.create_cart, name='create-cart'),

    path('api/items/delete', user_views.delete_item, name='delete-item'),
    path('api/carts/delete/<int:pk>', user_views.delete_cart, name='delete-cart'),

    # Views
    path('cart/<int:pk>', user_views.cart_detail, name='cart'),
    path('', user_views.cart_list, name='carts-list'),
]
