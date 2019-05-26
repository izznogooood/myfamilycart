from django.urls import path

from . import views as user_views

app_name = 'cart'

urlpatterns = [
    # JavaScript API Endpoints
    path('api/items/create', user_views.create_item, name='create-item'),
    path('api/carts/create', user_views.create_cart, name='create-cart'),

    path('api/items/delete', user_views.delete_item, name='delete-item'),
    path('api/carts/delete/<int:pk>', user_views.delete_cart, name='delete-cart'),

    # Views
    path('cart/<int:pk>', user_views.cart_detail, name='cart'),
    path('cart/<int:pk>/share', user_views.share_cart, name='share-cart'),
    path('', user_views.cart_list, name='carts-list'),
]
