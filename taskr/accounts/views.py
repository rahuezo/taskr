# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, login, logout, get_user_model)
from django.contrib import messages


User = get_user_model()


def login_view(request):
    if request.method == 'POST':
        print request.path

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome, {0}'.format(user.username), extra_tags='login_success')
            return redirect('dashboard:index')
        else:
            messages.error(request, 'Your credentials are incorrect. Please try again.', extra_tags='login_error')
            return redirect('accounts:login')

    context = {

    }
    return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out", extra_tags="logout_success")
    return redirect('home:index')
