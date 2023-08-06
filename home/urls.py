from django.urls import path

from .views import (
    index,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    PositionListView,
    PositionCreateView,
    TaskTypeListView,
    TaskTypeCreateView
)

urlpatterns = [
    path('', index, name='index'),
    path('task/', TaskListView.as_view(), name="task-list"),
    path('task/<int:pk>/', TaskDetailView.as_view(), name="task-detail"),
    path('task/create/', TaskCreateView.as_view(), name="task-create"),
    path('worker/', WorkerListView.as_view(), name="worker-list"),
    path('worker/create/', WorkerCreateView.as_view(), name="worker-create"),
    path('worker/<int:pk>>', WorkerDetailView.as_view(), name="worker-detail"),
    path('position/', PositionListView.as_view(), name="position-list"),
    path('position/create/', PositionCreateView.as_view(), name="position-create"),
    path('task-type/', TaskTypeListView.as_view(), name="task-type-list"),
    path('task-type/create/', TaskTypeCreateView.as_view(), name="task-type-create"),
]

app_name = "home"
