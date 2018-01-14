# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from models import Job


@login_required(login_url='accounts:login')
def index(request):
    return redirect('dashboard:index')


@login_required(login_url='accounts:login')
def show_job_view(request, job_id):
    if Job.objects.filter(pk=job_id).exists():
        current_job = Job.objects.get(pk=job_id)

        context = {
            'current_job': current_job,
            'tasks': current_job.task_set.all().order_by('date'),
            'view': 'list',
        }

        if request.method == 'GET' and request.GET.get('view'):
            context['view'] = request.GET.get('view')
    else:
        context = {
            'error': True,
        }
    return render(request, 'jobs/jobs.html', context)



