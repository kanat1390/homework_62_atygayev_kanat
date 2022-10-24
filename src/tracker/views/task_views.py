from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from tracker.models import Project, Task
from django.urls import reverse
from tracker.forms import SearchForm
from tracker.forms import TaskForm
from .mixin import SuccessDetailUrlMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskListView(ListView):
    model = Task
    template_name = 'tracker/task_list.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        search_form = SearchForm()
        context['search_form'] = search_form
        return context

    def get_queryset(self):
        text = self.request.GET.get('search', '')
        task_list = self.model.task_objects.all().order_by('-updated_at')
        if text:
            task_list = task_list.filter(
                summary__icontains=text).order_by('-updated_at')
        return task_list


class TaskDetailView(DetailView):
    model = Task
    template_name: str = 'tracker/task_detail.html'


class TaskCreateView(SuccessDetailUrlMixin, LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tracker/forms/task_form.html'
    detail_url_name = 'task-detail'
    form_class = TaskForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание задачи'
        return context


class TaskUpdateView(SuccessDetailUrlMixin, LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'tracker/forms/task_form.html'
    detail_url_name = 'task-detail'
    form_class = TaskForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование задачи'
        return context


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task

    def get_success_url(self):
        return reverse('task-list')
