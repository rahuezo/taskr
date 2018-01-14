from django.conf.urls import url, include
from . import views

app_name = 'dashboard'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^jobs/', include('jobs.urls')),
    url(r'^tasks/', include('tasks.urls')),
]
