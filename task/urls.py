from django.conf.urls import patterns, url

from task.views import TaskListView, TaskNewView

urlpatterns = patterns('',
    url(r'^todo/$', TaskListView.as_view(), name='todo_list'),
    url(r'^todo/task/create/$', TaskNewView.as_view(), name='task_new'),
)

