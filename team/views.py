from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import AddTask, Register
from .forms import AddTaskForm, RegistrationForm, RegisterForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User


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
    user = User.objects.all()

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
        context = {'forms': form, 'task': tasks, 'user': user}

        # Render the addtask.html template with the context
        return render(request, 'addtask.html', context)

def view_task(request, id):
    # Retrieve the task object with the specified id from the database
    task = AddTask.objects.get(id=id)
    
    # Create a context dictionary with the retrieved task object
    context = {"tasks": task}
    
    # Render the 'view_task.html' template with the context data
    return render(request, 'view_task.html', context)


def delete_task(request, id):
    # Check if the request method is POST
    if request.method == "POST":
        # Retrieve the task object with the specified id from the database
        task = AddTask.objects.get(id=id)
        
        # Delete the task from the database
        task.delete()
        
        # Add a success message to the current request's messages framework
        messages.success(request, "Task deleted")
        
        # Redirect the user to the 'index' URL
        return HttpResponseRedirect(reverse('index'))

    
def edit_task(request, id):
    # Check if the request method is POST
    if request.method == "POST":
        # Retrieve the task object with the specified id from the database
        task = AddTask.objects.get(id=id)

        # Create a form instance with the POST data and the retrieved task as the instance
        form = AddTaskForm(request.POST, instance=task)

        # Check if the form data is valid
        if form.is_valid():
            # Save the updated form data to the task object
            form.save()

            # Add a success message to the current request's messages framework
            messages.success(request, "Task updated successfully")

            # Redirect the user to the 'view_task' URL, passing the updated task's id as a parameter
            return redirect("view_task", id=id)

    else:
        # If the request method is not POST, retrieve the task object with the specified id from the database
        task = AddTask.objects.get(id=id)

        # Create a form instance with the retrieved task as the instance
        form = AddTaskForm(instance=task)

    # Create a context dictionary containing the form and task objects
    context = {'forms': form, 'task': task}

    # Render the 'edit_task.html' template with the context data
    return render(request, 'edit_task.html', context)


def Message(request):
    user = User.objects.all()
    # Retrieve all 'User' objects from the database
    
    messages = Register.objects.all()
    # Retrieve all 'Register' objects (messages) from the database
    
    if request.method == "POST":
        # Create a RegisterForm instance with the submitted data
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            # Extract the cleaned data from the form
            username = form.cleaned_data['username']
            message = form.cleaned_data['message']
            
            # Create a new message object using the extracted data
            message_object = Register.objects.create(
                username=username,
                message=message
            )
            
            # Redirect the user to the 'message' page
            return redirect('message')

    else:
        # Create an empty RegisterForm instance
        form = RegisterForm()

    # Prepare the context data to be passed to the template
    context = {'forms': form, 'messages': messages, 'user': user}
    
    # Render the 'Message.html' template with the form, messages, and user objects
    return render(request, 'Message.html', context)


def register(request):
    # Retrieve all user objects from the database
    user = User.objects.all()
    
    if request.method == 'POST':
        # Create a RegistrationForm instance with the submitted data
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            # Save the form data and create a new user
            user = form.save()
            
            # Redirect the user to the 'register' page
            return redirect('register')
    else:
        # Create an empty RegistrationForm instance
        form = RegistrationForm()
    
    # Render the 'register.html' template with the form and user objects
    return render(request, 'register.html', {'forms': form, 'user': user})


