from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from home.models import (
    Task,
    Worker,
    Position
)


def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')


class TaskListView(generic.ListView):
    model = Task


class WorkerListView(generic.ListView):
    model = Worker


class PositionListView(generic.ListView):
    model = Position


