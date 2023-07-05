from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import AddTask
from .forms import AddTaskForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def index(request):
    # Retrieve all tasks from the database
    tasks = AddTask.objects.all()

    # Prepare the context dictionary with the tasks data
    context = {'tasks': tasks}

    # Render the index.html template with the provided context
    return render(request, "index.html", context)


def add_task(request):
    # Create an instance of the AddTaskForm
    form = AddTaskForm()

    # Get all existing tasks from the database
    tasks = AddTask.objects.all()

    # Check if the request method is POST (i.e., form submission)
    if request.method == 'POST':
        # Create a new instance of the AddTaskForm with the submitted data
        form = AddTaskForm(request.POST)

        # Check if the form data is valid
        if form.is_valid():
            # Extract the cleaned data from the form
            task_name = form.cleaned_data['task_name']
            assigned_name = form.cleaned_data['assigned_name']
            date_assigned = form.cleaned_data['date_assigned']
            date_due = form.cleaned_data['date_due']
            task_details = form.cleaned_data['task_details']
            task_importance = form.cleaned_data['task_importance']
            completion_status = form.cleaned_data['completion_status']

            # Create a new AddTask object with the extracted data
            tasks_object = AddTask(
                task_name=task_name,
                assigned_name=assigned_name,
                date_assigned=date_assigned,
                date_due=date_due,
                task_details=task_details,
                task_importance=task_importance,
                completion_status=completion_status
            )

            # Save the new task object to the database
            tasks_object.save()

            # Display a success message
            messages.success(request, "Task added successfully")

            # Redirect to the index page
            return redirect("index")

    # If the request method is not POST (i.e., initial load or invalid form submission)
    else:
        # Create a new instance of the AddTaskForm
        form = AddTaskForm()

        # Prepare the context with the form and tasks data
        context = {'forms': form, 'task': tasks}

        # Render the addtask.html template with the context
        return render(request, 'addtask.html', context)

def view_task(request,id):
    task = AddTask.objects.get(id=id)
    context = {"tasks": task}
    return render(request, 'view_task.html', context)

def delete_task(request,id):
    if request.method == "POST":
        task = AddTask.objects.get(id=id)
        task.delete()
        messages.success(request,"Task deleted")
        return HttpResponseRedirect (reverse('index'))
    
def edit_task(request, id):
    if request.method == "POST":
        task = AddTask.objects.get(id=id)
        form = AddTaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully")
            return redirect("view_task", id=id)

    else:
        task = AddTask.objects.get(id=id)
        form = AddTaskForm(instance=task)

    context = {'forms': form, 'task': task}
    return render(request, 'edit_task.html', context)