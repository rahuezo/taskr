from django.conf.urls import url
from . import views

app_name = 'jobs'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<job_id>[0-9]+)/$', views.show_job_view, name='show_job'),
]
