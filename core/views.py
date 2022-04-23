from datetime import date, timedelta


from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView,
)
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy as rl

from .models import Task

# Create your views here.


class TaskList(LoginRequiredMixin, ListView):
    queryset = Task.objects.all()
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['incomplete_count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''

        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)
        
        context['search_input'] = search_input
        return context

class TaskDoneList(LoginRequiredMixin, ListView):
    queryset = Task.objects.all()
    context_object_name = 'tasks'
    template_name = 'core/task_done_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        one_week = date.today() - timedelta(days=7)
        context['tasks'] = context['tasks'].filter( 
            Q(user=self.request.user) & 
            Q(complete=True) & 
            Q(created_on__gt=one_week)
        ).order_by('-created_on')

        context['complete_count'] = context['tasks'].count()

        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    queryset = Task.objects.all()
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin, CreateView):
    queryset = Task.objects.all()
    template_name = 'core/task_create.html'         # mandatory
    fields = ['title', 'description', 'complete']
    success_url = rl('task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    queryset = Task.objects.all()
    template_name = 'core/task_update.html'         # mandatory
    fields = ['title', 'description', 'complete']
    success_url = rl('task-list')


class TaskDelete(LoginRequiredMixin, DeleteView):
    queryset = Task.objects.all()
    template_name = 'core/task_delete.html'         # mandatory

    success_url = rl('task-list')