from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from home.forms import WorkerCreationForm, TaskForm, WorkerUpdateForm, TaskSearchForm, WorkerSearchForm, \
    PositionSearchForm, TaskTypeSearchForm
from home.models import (
    Task,
    Worker,
    Position,
    TaskType
)


@login_required
def index(request):
    return render(request, 'pages/index.html')


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 10
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = TaskSearchForm(initial={
            "name": name
        })

        return context

    def get_queryset(self):
        queryset = Task.objects.all().prefetch_related("assignees")

        form = TaskSearchForm(data=self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "forms/task_form.html"
    success_url = reverse_lazy("home:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "forms/task_form.html"
    success_url = reverse_lazy("home:task-list")


@login_required
def toggle_complete_to_task(request, worker_id, task_id):
    task = Task.objects.get(id=task_id)
    if task.is_completed:  # probably could check if car exists
        task.is_completed = False
    else:
        task.is_completed = True

    task.save()

    return HttpResponseRedirect(reverse_lazy("home:worker-detail", args=[worker_id]))


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = WorkerSearchForm(initial={
            "name": name
        })

        return context

    def get_queryset(self):
        queryset = get_user_model().objects.all().select_related("position")

        form = TaskSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                Q(first_name__icontains=form.cleaned_data["name"]) |
                Q(last_name__icontains=form.cleaned_data["name"])
            )


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    queryset = Worker.objects.all().select_related("position")

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(WorkerDetailView, self).get_context_data(**kwargs)

        # Transform path to array
        path_to_arr = self.request.path.split('/')
        # Get worker id from array
        worker_id = path_to_arr[len(path_to_arr) - 1]
        # Get worker from db
        worker = get_user_model().objects.get(id=worker_id)
        # Transform queryset to list that counting of tasks
        tasks = list(worker.tasks.all().values())

        if tasks:
            count_of_completed_tasks = 0

            for task in tasks:
                if task["is_completed"]:
                    count_of_completed_tasks += 1

            progress = round(count_of_completed_tasks / len(tasks) * 100)
            contex["progress"] = progress

        contex["num_of_tasks"] = len(tasks)

        return contex


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    template_name = "forms/worker_form.html"


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    template_name = "forms/position_form.html"


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    paginate_by = 10
    context_object_name = "position_list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PositionListView, self).get_context_data(**kwargs)

        position = self.request.GET.get("position", "")

        context["search_form"] = PositionSearchForm(initial={
            "position": position
        })

        return context

    def get_queryset(self):
        queryset = Position.objects.all()

        form = PositionSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                position__icontains=form.cleaned_data["position"]
            )


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    template_name = "forms/position_form.html"
    success_url = reverse_lazy("home:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    template_name = "forms/position_form.html"
    success_url = reverse_lazy("home:position-list")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "home/task_type_list.html"
    context_object_name = "task_type_list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskTypeListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = TaskTypeSearchForm(initial={
            "name": name
        })

        return context

    def get_queryset(self):
        queryset = TaskType.objects.all()

        form = TaskTypeSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    template_name = "forms/task_type_form.html"
    success_url = reverse_lazy("home:task-type-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    template_name = "forms/task_type_form.html"
    success_url = reverse_lazy("home:task-type-list")

