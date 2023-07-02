from django.shortcuts import render, redirect
from .models import AddTask
from .forms import AddTaskForm
from django.contrib import messages

# Create your views here.
def index(request):
    tasks = AddTask.objects.all()
    context = {'tasks': tasks}
    return render(request, "index.html", context)

def add_task(request):
    form = AddTaskForm()
    tasks = AddTask.objects.all()

    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task_name = form.cleaned_data['task_name']
            assigned_name = form.cleaned_data['assigned_name']
            date_assigned = form.cleaned_data['date_assigned']
            date_due = form.cleaned_data['date_due']
            task_details = form.cleaned_data['task_details']
            task_importance = form.cleaned_data['task_importance']
            completion_status = form.cleaned_data['completion_status']

            tasks_object = AddTask(task_name=task_name, assigned_name=assigned_name,date_assigned=date_assigned, date_due=date_due, task_details=task_details,  task_importance=task_importance, completion_status=completion_status)
            tasks_object.save()

            messages.success(request, "Task added successfully")
            return redirect("index")
    else:
        form = AddTaskForm()
        context = {'forms':form, 'task':tasks}
        return render(request, 'addtask.html', context)