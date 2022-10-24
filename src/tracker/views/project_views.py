from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from tracker.models import Project
from django.urls import reverse
from tracker.forms import ProjectForm
from django.core.paginator import Paginator
from .mixin import SuccessDetailUrlMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


class ProjectListView(ListView):
    model = Project
    template_name = 'tracker/project_list.html'
    ordering = ['-started_date']
    queryset = Project.project_objects.all()


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'tracker/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = context['project'].tasks.all()
        paginator = Paginator(tasks, per_page=6)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context


class ProjectCreateView(SuccessDetailUrlMixin, LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'tracker/forms/project_form.html'
    detail_url_name = 'project-detail'
    form_class = ProjectForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание проекта'
        return context


class ProjectUpdateView(SuccessDetailUrlMixin, LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'tracker/forms/project_form.html'
    detail_url_name = 'project-detail'
    form_class = ProjectForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование проекта'
        return context


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project

    def get_success_url(self):
        return reverse('project-list')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.is_deleted = True
        self.object.save()
        return HttpResponseRedirect(success_url)
