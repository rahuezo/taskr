# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from jobs.models import Job


@login_required(login_url='accounts:login')
def index(request):
    context = {
        'jobs': Job.objects.order_by('-modified'),
    }
    return render(request, 'dashboard/dashboard.html', context)

