from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseNotAllowed, HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddTaskForm, SearchForm
from .models import TaskModel


# Create your views here.
def home(request):
    return render(request, 'taskhero/home.html')

# Add try and excepts to the code for the 404 and 505 error pages
@login_required
def dashboard(request):
    all_tasks = TaskModel.objects.filter(added_by=request.user)
    to_do_tasks = all_tasks.filter(status='TD')
    in_progress_tasks = all_tasks.filter(status='IP')
    completed_tasks = all_tasks.filter(status='CPD')
    search_form = SearchForm(request.GET)
    if request.method == 'GET':
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            title = search_form.cleaned_data.get('title')
            if title:
                all_tasks = all_tasks.filter(title__icontains=title)

    context = {
        'all_tasks': all_tasks,
        'to_do_tasks': to_do_tasks,
        'in_progress_tasks': in_progress_tasks,
        'completed_tasks': completed_tasks,
        'search_form': search_form,
    }
    return render(request, 'taskhero/dashboard.html', context)

@login_required
def add_task(request):
    task_form = AddTaskForm(request.POST)
    if request.method == 'POST':
        task_form = AddTaskForm(request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.added_by = request.user
            task.save()
            messages.success(request, 'Task succesfully added')
            return redirect('TaskHero:dashboard')
    context = {
        'task_form': task_form,
    }
    return render(request, 'taskhero/add-task.html', context)

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)
    if task.added_by != request.user:
        return render(request, 'https/forbidden.html')
    is_overdue = task.due_date and task.due_date < timezone.now().date() and task.status != 'CPD'
    return render(request, 'taskhero/task-detail.html', context={'task': task, 'is_overdue': is_overdue})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)
    edit_form = AddTaskForm(instance=task)
    if task.added_by != request.user:
        return render(request, 'https/forbidden.html')
    if request.method == 'POST':
        edit_form = AddTaskForm(request.POST, instance=task, )
        
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'Task edited succesfully')
            return redirect(reverse('TaskHero:task_detail', kwargs={'task_id': task_id}))
    context = {
        'edit_form': edit_form,
        'task': task,
    }
    return render(request, 'taskhero/edit-task.html', context)

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)
    if task.added_by != request.user:
        return render(request, 'https/forbidden.html')
    # task_form = AddTaskForm(instance=task)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted succesfully')
        return redirect('TaskHero:dashboard')
    context = {
        'task': task
    }
    return render(request, 'taskhero/confirm-delete.html', context)