from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from home.models import Task, Worker


def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')


class TaskListView(generic.ListView):
    model = Task
    template_name = "home/task_list.html"


class WorkerListView(generic.ListView):
    model = Worker
    template_name = "home/worker_list.html"


