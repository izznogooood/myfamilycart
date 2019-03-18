from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required

from .models import Item, Cart
from users.models import Word

import bleach

# ######################## User views #########################


@login_required
def cart_detail(request, pk):
    try:
        cart = Cart.objects.get(id=pk, user=request.user)
    except Cart.DoesNotExist:
        return HttpResponseNotFound('404')

    items = cart.items.all()

    context = {'items': items,
               'cart': cart}

    return render(request, 'cart/cart-detail.html', context)


@login_required
def cart_list(request):
    context = {'carts': Cart.objects.all().filter(user=request.user)}

    return render(request, 'cart/cart-list.html', context)


# ################## JavaScript API Endpoints ##################


@login_required
def create_item(request):
    if request.method == 'POST':
        data = request.POST

        cart_id = data['cart']
        name = bleach.clean(data['name'].rstrip().lstrip())
        quantity = data['quantity']
        user = request.user

        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            return HttpResponseNotFound('404')

        if not user.id == cart.user.id:
            return HttpResponseNotFound('404')
        else:
            item = Item(quantity=quantity, name=name, cart_id=cart_id)
            item.save()

            # Saving words for use with form autocomplete
            c_name = name.capitalize()
            try:
                word = Word.objects.get(user=user, name=c_name)
            except Word.DoesNotExist:
                word = None

            if word:
                word.count += 1
                word.save()
            else:
                word = Word(user=user, name=c_name, count=1)
                word.save()

            return JsonResponse({'quantity': item.quantity, 'name': item.name})

    else:
        return HttpResponseNotFound('404')


@login_required
def create_cart(request):
    if request.method == 'POST':

        data = request.POST
        name = bleach.clean(data['name'].rstrip().lstrip())
        user = request.user

        _cart = Cart(user=user, name=name)
        _cart.save()

        return JsonResponse({'name': _cart.name, 'id': _cart.id, 'url': _cart.get_absolute_url()})
    else:
        return HttpResponseNotFound('404')


@login_required
def delete_item(request):
    if request.method == 'POST':
        data = request.POST

        try:
            cart = Cart.objects.get(id=data['cart'])
            if not request.user.id == cart.user.id:
                return HttpResponseNotFound('404')

        except Cart.DoesNotExist:
            return HttpResponseNotFound('404')

        items = Item.objects.all().filter(name=data['name'], quantity=data['quantity'], cart_id=data['cart'])
        items.delete()

        return JsonResponse({'success': True})
    else:
        return HttpResponseNotFound('404')


@login_required
def delete_cart(request, pk):
    try:
        _cart = Cart.objects.all().filter(id=pk, user=request.user)
        _cart.delete()

        return redirect('cart:carts-list')

    except Cart.DoesNotExist:
        return HttpResponseNotFound('404')











