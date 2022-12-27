from django.urls import path

from task.views import (
    TaskListView,
    TaskAddView,
    TaskDeleteView,
    TaskUpdateView,
    TagListView,
    TagAddView,
    TagUpdateView,
    TagDeleteView,
    toggle_done_task
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/add/", TaskAddView.as_view(), name="task-add"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "tasks/<int:pk>/toggle-assign/",
        toggle_done_task,
        name="toggle-task-done",
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/add/", TagAddView.as_view(), name="tag-add"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "task"
