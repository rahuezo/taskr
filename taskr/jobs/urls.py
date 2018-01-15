from django.conf.urls import url
from . import views
from tasks.views import delete_task_view

app_name = 'jobs'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<job_id>[0-9]+)/$', views.show_job_view, name='show_job'),
    url(r'^delete-task/(?P<job_id>[0-9]+)/$', delete_task_view, name='delete_task'),
    url(r'add-job/$', views.add_job_view, name='add_job'),
]
