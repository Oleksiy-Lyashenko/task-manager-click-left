from django.urls import path

from .views import (
    index,
    TaskListView,
    WorkerListView,
    PositionListView
)

urlpatterns = [
    path('', index, name='index'),
    path('task/', TaskListView.as_view(), name="task-list"),
    path('worker/', WorkerListView.as_view(), name="worker-list"),
    path('position/', PositionListView.as_view(), name="position-list"),
]

app_name = "home"
