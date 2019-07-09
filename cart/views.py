import bleach
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template.loader import get_template

from users.models import Word
from .forms import ShareCartForm
from .models import Item, Cart


# ######################## User views #########################


@login_required
def cart_detail(request, pk):
    user_id = request.user.id
    shared = False

    try:
        cart = Cart.objects.get(id=pk)
    except Cart.DoesNotExist:
        return HttpResponseNotFound('404')

    if user_id != cart.owner.id:
        shared = True
        try:
            assert cart.shared_with.get(id=user_id).id
        except User.DoesNotExist:
            return HttpResponseNotFound('404')

    context = {'cart': cart, 'shared': shared}

    return render(request, 'cart/cart-detail.html', context)


@login_required
def cart_list(request):
    return render(request, 'cart/cart-list.html')


@login_required
def share_cart(request, pk):
    form = ShareCartForm()
    cart = Cart.objects.get(id=pk)
    user = None

    if request.method == 'POST':
        form = ShareCartForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username', None)
            email = form.cleaned_data.get('email', None)

            if username:
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    messages.warning(request, 'Username does not exist!')

            else:
                try:
                    user = User.objects.get(email=email)
                except User.DoesNotExist:
                    # todo: Automatic creation of user and email password reset / login
                    messages.warning(request, f'A user with email: "{email}"" does not exist!')

            if user == request.user:
                messages.warning(request, 'Schizophrenia Warning, consider seeing a doctor.')
                return redirect('cart:cart', pk=cart.id)

            if user:
                subject = f'MyFamily: {request.user.username} shared a cart with you.'
                to = [user.email]
                from_email = 'noreply@unialt.no'
                # uri = request.META['HTTP_HOST']
                context = {
                    'username': user.username,
                    'sender': request.user.username
                }
                message = get_template('cart/email-share.html').render(context)
                msg = EmailMessage(subject, message, to=to, from_email=from_email)
                msg.content_subtype = 'html'
                msg.send()

                cart.shared_with.add(user)
                messages.success(request, "User notified, you've shared your cart!")

                return redirect('cart:cart', pk=cart.id)

    return render(request, 'cart/cart-share.html', {'form': form, 'cart': cart})


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

        if user.id != cart.owner.id:
            try:
                assert cart.shared_with.get(id=user.id).id
            except User.DoesNotExist:
                return HttpResponseNotFound('404')

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

        _cart = Cart(owner=user, name=name)
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
        except Cart.DoesNotExist:
            return HttpResponseNotFound('404')

        if request.user.id != cart.owner.id:
            try:
                assert cart.shared_with.get(id=request.user.id).id
            except User.DoesNotExist:
                return HttpResponseNotFound('404')

        items = Item.objects.all().filter(name=data['name'], quantity=data['quantity'], cart_id=data['cart'])
        items.delete()

        return JsonResponse({'success': True})
    else:
        return HttpResponseNotFound('404')


@login_required
def delete_cart(request, pk):
    try:
        cart = Cart.objects.all().filter(id=pk, owner=request.user)
        cart.delete()

        return redirect('cart:carts-list')

    except Cart.DoesNotExist:
        return HttpResponseNotFound('404')
