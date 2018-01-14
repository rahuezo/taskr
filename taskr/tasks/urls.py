from django.conf.urls import url
from . import views

app_name = 'tasks'


urlpatterns = [
    url(r'add-task/$', views.add_task_view, name='add_task'),
]
