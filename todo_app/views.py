from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todo/task_detail.html', {'task': task})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def task_add(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')
        Task.objects.create(description=description, status=status, due_date=due_date)
        return redirect('task_list')
    return render(request, 'todo/task_form.html')