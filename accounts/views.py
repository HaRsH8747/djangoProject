# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from djangoProject.middleware import get_active_sessions

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            is_seller = request.POST.get('is_seller') == 'on'
            UserProfile.objects.create(user=user, is_seller=is_seller)
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('product_list')

@login_required
def profile(request):
    visits = request.session.get('visits', 0)
    active_sessions = get_active_sessions()
    return render(request, 'accounts/profile.html', {'visits': visits, 'active_sessions': active_sessions})
