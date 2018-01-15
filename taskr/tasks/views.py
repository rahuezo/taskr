# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from jobs.models import Job
from models import Task
from django.contrib.auth import get_user_model
from activity_log.models import Activity


User = get_user_model()


@login_required(login_url='accounts:login')
def add_task_view(request):
    if request.method == 'POST':
        title = request.POST.get('task-title')
        date = request.POST.get('task-date')
        start = request.POST.get('task-start')
        end = request.POST.get('task-end')
        notes = request.POST.get('task-notes')
        job_id = request.POST.get('job-id')

        new_task = Task(job=Job.objects.get(pk=job_id), title=title, date=date, start=start, end=end, notes=notes)
        new_task.save()

        new_activity = Activity(user=User.objects.get(username=request.user.username),
                                description="Added new task <strong>{0}</strong> to <strong>{1}</strong>".format(title,
                                                                                                Job.objects.get(pk=job_id).title))
        new_activity.save()

        return redirect('dashboard:index')


    context = {}
    return render(request, '', context)


@login_required(login_url='accounts:login')
def delete_task_view(request, job_id):
    if request.method == 'POST':
        task_id = request.POST.get('task-id')

        current_task = Task.objects.get(pk=task_id)
        deleted_task_title = current_task.title
        current_task.delete()

        icon = '<i class="fa fa-calendar-minus-o text-danger" aria-hidden="true"></i>'
        new_activity = Activity(user=User.objects.get(username=request.user.username),
                                icon=icon,
                                description="Deleted task <strong>{0}</strong> from <strong>{1}</strong>".format(deleted_task_title,
                                                                                                Job.objects.get(
                                                                                                    pk=job_id).title))
        new_activity.save()
        return redirect('dashboard:index')
    context = {}
    return render(request, 'dashboard/dashboard.html', context)
