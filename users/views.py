from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect

from .forms import RegisterForm, UpdateUserForm
from .models import Word


# ######################## User views #########################


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(request,
                                    username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)

            messages.success(request, f'Welcome in, {form.cleaned_data.get("username")}!')
            return redirect('cart:carts-list')

    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def about(request):
    return render(request, 'about.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Profile Info Updated')
    else:
        u_form = UpdateUserForm(instance=request.user)

    p_form = PasswordChangeForm(request.user)

    return render(request, 'users/profile.html', {'u_form': u_form, 'p_form': p_form})


@login_required
def del_user(request):
    user = User(id=request.user.id)
    user.delete()

    auth.logout(request)

    messages.success(request, 'Your account has been deleted!')

    return redirect('login')


@login_required
def top50(request):
    return render(request, 'users/top50.html')


@login_required
def change_password(request):
    """
    Redirects to Profile if change = success.
    Or renders a new profile page with errors
    """
    u_form = UpdateUserForm(instance=request.user)

    if request.method == 'POST':
        p_form = PasswordChangeForm(request.user, request.POST)
        if p_form.is_valid():
            user = p_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = PasswordChangeForm(request.user)

    return render(request, 'users/profile.html', {'p_form': p_form, 'u_form': u_form})


# ######################## API / USER Endpoints #########################


@login_required
def delete_words(request):
    user = request.user

    words = Word.objects.all().filter(user=user)
    words.delete()

    return redirect('top50')


@login_required
def delete_word_item(request, pk):
    try:
        item = Word.objects.get(id=pk, user=request.user)
        item.delete()

        return JsonResponse({'success': 'true'})

    except Word.DoesNotExist:
        return HttpResponseNotFound('404')
