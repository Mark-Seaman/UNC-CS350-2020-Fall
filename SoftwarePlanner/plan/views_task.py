from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Task


class TaskView(RedirectView):
    url = reverse_lazy('task_list')


class TaskListView(ListView):
    template_name = 'task/list.html'
    model = Task
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    template_name = 'task/detail.html'
    model = Task
    context_object_name = 'task'

    # def get_context_data(self, **kwargs):
    #     kwargs = super().get_context_data(**kwargs)
    #     task = kwargs.get('task')
    #     kwargs['dependents'] = task.dependents
    #     return kwargs


class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = "task/add.html"
    model = Task
    fields = '__all__'

    # def form_valid(self, form):
    #     form.instance.book = 1
    #     form.instance.author = Person.get_me(self.request.user)
    #     return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "task/edit.html"
    model = Task
    fields = '__all__'


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task/delete.html'
    success_url = reverse_lazy('task_list')
