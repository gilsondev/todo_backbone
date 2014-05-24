from django.conf.urls import patterns, url

from task.views import TaskListView, TaskNewView, TaskUpdateView

urlpatterns = patterns('',
    url(r'^todo/$', TaskListView.as_view(), name='todo_list'),
    url(r'^todo/task/create/$', TaskNewView.as_view(), name='task_new'),
    url(r'^todo/task/(?P<pk>[\d+])/$', TaskUpdateView.as_view(),
        name='task_update'),
)
