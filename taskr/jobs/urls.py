from django.conf.urls import url
from . import views
from tasks.views import delete_task_view

app_name = 'jobs'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<job_id>[0-9]+)/$', views.show_job_view, name='show_job'),
    url(r'^delete-task/$', delete_task_view, name='delete_task'),
    url(r'^delete-job/$', views.delete_job_view, name='delete_job'),
    url(r'^edit-job/$', views.edit_job_view, name='edit_job'),
    url(r'add-job/$', views.add_job_view, name='add_job'),
]
