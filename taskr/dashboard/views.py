# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


User = get_user_model()


@login_required(login_url='accounts:login')
def index(request):
    context = {
        'jobs': User.objects.get(username=request.user.username).job_set.order_by('-modified'),
    }
    return render(request, 'dashboard/dashboard.html', context)

