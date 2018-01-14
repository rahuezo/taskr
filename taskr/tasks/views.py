# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from jobs.models import Job
from models import Task


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

        return redirect('dashboard:index')


    context = {}
    return render(request, '', context)