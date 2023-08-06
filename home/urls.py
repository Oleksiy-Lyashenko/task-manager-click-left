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
    PositionListView,
    PositionCreateView,
    PositionUpdateView,
    TaskTypeListView,
    TaskTypeCreateView,
    TaskTypeUpdateView
)

urlpatterns = [
    path('', index, name='index'),
    path('task/', TaskListView.as_view(), name="task-list"),
    path('task/<int:pk>/', TaskDetailView.as_view(), name="task-detail"),
    path('task/create/', TaskCreateView.as_view(), name="task-create"),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name="task-update"),
    path('worker/', WorkerListView.as_view(), name="worker-list"),
    path('worker/create/', WorkerCreateView.as_view(), name="worker-create"),
    path('worker/<int:pk>>', WorkerDetailView.as_view(), name="worker-detail"),
    path('worker/<int:pk>>/update/', WorkerUpdateView.as_view(), name="worker-update"),
    path('position/', PositionListView.as_view(), name="position-list"),
    path('position/create/', PositionCreateView.as_view(), name="position-create"),
    path('position/<int:pk>/update/', PositionUpdateView.as_view(), name="position-update"),
    path('task-type/', TaskTypeListView.as_view(), name="task-type-list"),
    path('task-type/create/', TaskTypeCreateView.as_view(), name="task-type-create"),
    path('task-type/<int:pk>/update/', TaskTypeUpdateView.as_view(), name="task-type-update"),

]

app_name = "home"
