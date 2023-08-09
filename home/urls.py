from django.urls import path

from .views import (
    index,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerUpdateView,
    toggle_complete_to_task,
    PositionListView,
    PositionCreateView,
    PositionUpdateView,
    TaskTypeListView,
    TaskTypeCreateView,
    TaskTypeUpdateView
)

urlpatterns = [
    path('', index, name='index'),
    path('tasks/', TaskListView.as_view(), name="task-list"),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name="task-detail"),
    path('tasks/create/', TaskCreateView.as_view(), name="task-create"),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name="task-update"),
    path('workers/', WorkerListView.as_view(), name="worker-list"),
    path('workers/create/', WorkerCreateView.as_view(), name="worker-create"),
    path('workers/<int:pk>', WorkerDetailView.as_view(), name="worker-detail"),
    path('workers/<int:pk>/update/', WorkerUpdateView.as_view(), name="worker-update"),
    path('workers/<int:worker_id>/toggle-complete/<int:task_id>', toggle_complete_to_task, name="toggle-task-complete"),
    path('positions/', PositionListView.as_view(), name="position-list"),
    path('positions/create/', PositionCreateView.as_view(), name="position-create"),
    path('positions/<int:pk>/update/', PositionUpdateView.as_view(), name="position-update"),
    path('task-types/', TaskTypeListView.as_view(), name="task-type-list"),
    path('task-types/create/', TaskTypeCreateView.as_view(), name="task-type-create"),
    path('task-types/<int:pk>/update/', TaskTypeUpdateView.as_view(), name="task-type-update"),

]

app_name = "home"
