# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from jobs.models import Job
from models import Task
from django.contrib.auth import get_user_model
from activity_log.models import Activity
from django.contrib import messages
from datetime import datetime

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

        added_msg = "Added new task <strong>{0}</strong> to <strong>{1}</strong>".format(title, Job.objects.get(pk=job_id).title)
        icon = '<i class="fa fa-plus text-success" aria-hidden="true"></i>'
        new_activity = Activity(user=User.objects.get(username=request.user.username),
                                icon=icon,
                                description=added_msg)
        new_activity.save()
        messages.success(request, added_msg, extra_tags='added_task')

    return redirect('dashboard:index')


@login_required(login_url='accounts:login')
def edit_task_view(request):
    if request.method == 'POST':
        title = request.POST.get('task-title')
        date = request.POST.get('task-date')
        start = request.POST.get('task-start')
        end = request.POST.get('task-end')
        notes = request.POST.get('task-notes')
        job_id = request.POST.get('job-id')
        task_id = request.POST.get('task-id')

        task_to_edit = Task.objects.get(pk=task_id)

        edit_items = []

        if task_to_edit.title != title:
            edit_items.append("""<p>{0} <i class="fa fa-long-arrow-right" 
            aria-hidden="true"></i> {1} </p>""".format(task_to_edit.title, title))
        if str(task_to_edit.date).split()[0] != date:
            edit_items.append("""<p>{0} <i class="fa fa-long-arrow-right" 
            aria-hidden="true"></i> {1} </p>""".format(str(task_to_edit.date).split()[0], date))
        if task_to_edit.notes != notes:
            edit_items.append("""<p>{0} <i class="fa fa-long-arrow-right" 
                        aria-hidden="true"></i> {1} </p>""".format(task_to_edit.notes, notes))

        task_to_edit.title = title
        task_to_edit.created = datetime.strptime(date, '%Y-%m-%d')
        task_to_edit.notes = notes
        task_to_edit.start = start
        task_to_edit.end = end
        task_to_edit.save()

        icon = '<i class="fa fa-pencil text-success" aria-hidden="true"></i>'
        edited_msg = """Edited Task <strong>{0}</strong>{1}""".format(title, ''.join(edit_items))

        new_activity = Activity(user=User.objects.get(username=request.user.username),
                                icon=icon,
                                description=edited_msg)
        new_activity.save()

        messages.success(request, edited_msg, extra_tags='edited_task')

    return redirect('dashboard:index')


@login_required(login_url='accounts:login')
def delete_task_view(request):
    if request.method == 'POST':
        job_id = request.POST.get('job-id')
        task_id = request.POST.get('task-to-delete-id')

        current_task = Task.objects.get(pk=task_id)
        deleted_task_title = current_task.title
        current_task.delete()

        deleted_msg = "Deleted task <strong>{0}</strong> from <strong>{1}</strong>".format(deleted_task_title, Job.objects.get(pk=job_id).title)
        icon = '<i class="fa fa-trash text-danger" aria-hidden="true"></i>'
        new_activity = Activity(user=User.objects.get(username=request.user.username),
                                icon=icon,
                                description=deleted_msg)
        new_activity.save()
        messages.success(request, deleted_msg, extra_tags='deleted_task')
    return redirect('dashboard:index')

