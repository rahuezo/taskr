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


def register_view(request):
    if request.method == 'POST':
        print request.path

        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        valid_new_user = 1

        if User.objects.filter(username=username).exists():
            valid_new_user = 0
            messages.error(request, 'Username is already taken.', extra_tags='user_exists')

        if User.objects.filter(email=email).exists():
            valid_new_user = 0
            messages.error(request, 'Email is already taken.', extra_tags='email_exists')

        if password1 != password2:
            valid_new_user = 0
            messages.error(request, 'Both passwords must match.', extra_tags='password_unmatch')
        else:
            if len(password1) < 6:
                messages.error(request, 'Your password must be at least 6 characters long.',
                               extra_tags='password_length')

        if valid_new_user:
            print "All tests passed"
            new_user = User.objects.create_user(username=username, email=email,
                                                first_name=firstname, last_name=lastname, password=password1)
            login(request, new_user)
            messages.success(request, 'Welcome, {0}'.format(new_user.username), extra_tags='login_success')
            return redirect('dashboard:index')
        else:
            print "Cannot create new user"

        # user = authenticate(username=username, password=password)
        #
        # if user is not None:
        #     login(request, user)
        #     messages.success(request, 'Welcome, {0}'.format(user.username), extra_tags='login_success')
        #     return redirect('dashboard:index')
        # else:
        #     messages.error(request, 'Your credentials are incorrect. Please try again.', extra_tags='login_error')
        #     return redirect('accounts:login')

    context = {

    }
    return render(request, "accounts/register.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out", extra_tags="logout_success")
    return redirect('home:index')
