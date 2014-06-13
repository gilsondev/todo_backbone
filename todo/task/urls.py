from django.conf.urls import patterns, url

from todo.task.views import TaskListView, TaskUpdateView

urlpatterns = patterns('',
    url(r'^todo/$', TaskListView.as_view(), name='todo_listcreate'),
    url(r'^todo/(?P<pk>[\d+])/$', TaskUpdateView.as_view(),
        name='task_update'),
)

