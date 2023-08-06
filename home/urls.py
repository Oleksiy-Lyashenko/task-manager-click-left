from django.urls import path

from .views import (
    index,
    TaskListView,
    TaskDetailView,
    WorkerListView,
    WorkerDetailView,
    PositionListView,
    PositionCreateView,
    TaskTypeListView,
    TaskTypeCreateView
)

urlpatterns = [
    path('', index, name='index'),
    path('task/', TaskListView.as_view(), name="task-list"),
    path('task/<int:pk>/', TaskDetailView.as_view(), name="task-detail"),
    path('worker/', WorkerListView.as_view(), name="worker-list"),
    path('worker/<int:pk>>', WorkerDetailView.as_view(), name="worker-detail"),
    path('position/', PositionListView.as_view(), name="position-list"),
    path('position/create/', PositionCreateView.as_view(), name="position-create"),
    path('task-type/', TaskTypeListView.as_view(), name="task-type-list"),
    path('task-type/create/', TaskTypeCreateView.as_view(), name="task-type-create"),
]

app_name = "home"
