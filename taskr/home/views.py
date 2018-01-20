# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


def index(request):
    if request.user.is_authenticated():
        return redirect('dashboard:index')
    context = {}
    return render(request, 'home/home.html', context)
