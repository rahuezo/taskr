from django.conf.urls import url
from . import views

app_name = 'activity_log'


urlpatterns = [
    url(r'^$', views.index, name='index'),
]
