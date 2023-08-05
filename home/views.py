from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from home.models import (
    Task,
    Worker,
    Position,
    TaskType
)


def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all().prefetch_related("assignees")


class TaskDetailView(generic.DetailView):
    model = Task


class WorkerListView(generic.ListView):
    model = Worker
    queryset = Worker.objects.all().select_related("position")


class PositionListView(generic.ListView):
    model = Position


class TaskTypeListView(generic.ListView):
    model = TaskType
    template_name = "home/task_type_list.html"
    context_object_name = "task_type_list"
