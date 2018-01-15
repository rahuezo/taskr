# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Activity
from django.contrib.auth import get_user_model


User = get_user_model()


def index(request):
    context = {
        'activities': User.objects.get(username=request.user.username).activity_set.order_by('-created')
    }
    return render(request, 'activity_log/activity_log.html', context)
