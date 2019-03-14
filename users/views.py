from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from .models import Word
from .forms import RegisterForm, UpdateUserForm


# ######################## User views #########################


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account is ready, {form.cleaned_data.get("username")}!')
            return redirect('login')

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


@login_required
def delete_words(request):
    user = request.user

    words = Word.objects.all().filter(user=user)
    words.delete()

    return redirect('top50')


