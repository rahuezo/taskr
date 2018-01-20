# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from models import Job
from datetime import datetime
from django.contrib.auth import get_user_model
from activity_log.models import Activity
from django.contrib import messages

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

        icon = '<i class="fa fa-plus text-success" aria-hidden="true"></i>'
        added_msg = "Added new job <strong>{0}</strong>".format(title)
        new_activity = Activity(user=User.objects.get(username=request.user.username),
                                icon=icon,
                                description=added_msg)
        new_activity.save()

        messages.success(request, added_msg, extra_tags='added_job')

    return redirect('dashboard:index')


@login_required(login_url='accounts:login')
def edit_job_view(request):
    if request.method == 'POST':
        job_id = request.POST.get('job-id')
        title = request.POST.get('job-title')
        date = request.POST.get('job-date')
        description = request.POST.get('job-description')

        job_to_edit = Job.objects.get(pk=job_id)

        edit_items = []

        if job_to_edit.title != title:
            edit_items.append("""<p>{0} <i class="fa fa-long-arrow-right" 
            aria-hidden="true"></i> {1} </p>""".format(job_to_edit.title, title))
        if str(job_to_edit.created).split()[0] != date:
            edit_items.append("""<p>{0} <i class="fa fa-long-arrow-right" 
            aria-hidden="true"></i> {1} </p>""".format(str(job_to_edit.created).split()[0], date))
        if job_to_edit.description != description:
            edit_items.append("""<p>{0} <i class="fa fa-long-arrow-right" 
                        aria-hidden="true"></i> {1} </p>""".format(job_to_edit.description, description))

        job_to_edit.title = title
        job_to_edit.created = datetime.strptime(date, '%Y-%m-%d')
        job_to_edit.description = description
        job_to_edit.save()

        icon = '<i class="fa fa-pencil text-success" aria-hidden="true"></i>'
        added_msg = """Edited job <strong>{0}</strong>{1}""".format(title, ''.join(edit_items))

        new_activity = Activity(user=User.objects.get(username=request.user.username),
                                icon=icon,
                                description=added_msg)
        new_activity.save()

        messages.success(request, added_msg, extra_tags='edited_job')

    return redirect('dashboard:index')


@login_required(login_url='accounts:login')
def delete_job_view(request):
    if request.method == 'POST':
        job_id = request.POST.get('job-to-delete-id')
        current_job = Job.objects.get(pk=job_id)
        deleted_job_title = current_job.title
        current_job.delete()

        deleted_msg = "Deleted job <strong>{0}</strong>".format(deleted_job_title)
        icon = '<i class="fa fa-trash text-danger" aria-hidden="true"></i>'
        new_activity = Activity(user=User.objects.get(username=request.user.username),
                                icon=icon,
                                description=deleted_msg)
        new_activity.save()
        messages.success(request, deleted_msg, extra_tags='deleted_job')
    return redirect('dashboard:index')




