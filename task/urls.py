from django.conf.urls import patterns, url

from task.views import TaskListView

urlpatterns = patterns('',
    url(r'^todos/$', TaskListView.as_view(), name='task_list'),
)

