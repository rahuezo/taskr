# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from models import Job
from datetime import datetime
from django.contrib.auth import get_user_model
from activity_log.models import Activity


User = get_user_model()


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


@login_required(login_url='accounts:login')
def add_job_view(request):
    if request.method == 'POST':
        title = request.POST.get('job-title')
        date = request.POST.get('job-date')
        description = request.POST.get('job-description')

        user = User.objects.get(username=request.user.username)

        new_job = Job(user=user, title=title, description=description,
                      created=datetime.strptime(date, '%Y-%m-%d'))
        new_job.save()

        new_activity = Activity(user=User.objects.get(username=request.user.username),
                                description="Added new job <strong>{0}</strong>".format(title))
        new_activity.save()

        return redirect('dashboard:index')


    context = {}
    return render(request, '', context)



