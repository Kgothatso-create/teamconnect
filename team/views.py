from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import AddTask, Register
from .forms import AddTaskForm, RegistrationForm, RegisterForm, LoginForm, Pass_word_changeForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash


# Create your views here.
# index view for homepage
def index(request):
    # Retrieve the logged-in user
    user = request.user
    
    # Retrieve tasks based on user role
    if user.is_superuser:
        # For admin/superuser, retrieve all tasks
        tasks = AddTask.objects.all()
    else:
        # For simple users, retrieve only their tasks
        tasks = AddTask.objects.filter(assigned_name=user)

    # Prepare the context dictionary with the tasks data
    context = {'tasks': tasks}

    # Render the index.html template with the provided context
    return render(request, "index.html", context)

# view to add tasks
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

# view to see details of a task
def view_task(request, id):
    # Retrieve the task object with the specified id from the database
    task = AddTask.objects.get(id=id)
    
    # Create a context dictionary with the retrieved task object
    context = {"tasks": task}
    
    # Render the 'view_task.html' template with the context data
    return render(request, 'view_task.html', context)

# view to delete a task
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

# view to edit a task
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

# view for team members to message each other
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
    return render(request, 'message.html', context)

# view to add a user
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

# view to delete a message
def delete_message(request,id):
    # Check if the request method is POST
    if request.method == "POST":
        # Retrieve the message object with the specified id from the database
        messages = Register.objects.get(id=id)
        
        # Delete the message from the database
        messages.delete()
        
        # Redirect the user to the 'message' URL
        return HttpResponseRedirect(reverse('message'))

# login view
def login_view(request):
    if request.method == 'POST':
        # Initialize AuthenticationForm with request and POST data
        form = LoginForm(request, data=request.POST)

        # Check if form is valid
        if form.is_valid():
            # Get username from POST data
            username = request.POST['username']
            # Get password from POST data
            password = request.POST['password']
            # Authenticate user
            user = authenticate(request, username=username, password=password)

            # If user is authenticated, log in the user
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('index')

        # Show error message for invalid form
        else:
            messages.error(request, "Invalid username or password.")

    # Create an instance of AuthenticationForm
    form = LoginForm()
    context = {'forms': form}
    # Render login.html template with request and form data
    return render(request, 'login.html', context)

# User logout view
def logout_view(request):

    # Log out the user
    logout(request)

    # Show info message for successful logout
    messages.info(request, "You have successfully logged out.") 

    # Get the URL for the login page using URL reverse
    login_url = reverse('login')

    # Redirect to the login page
    return redirect(login_url)

# The view function for changing the user's password
def change_password(request):
    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = Pass_word_changeForm(request.user, request.POST)
        
        if form.is_valid():
            # If the form is valid, save the new password for the user
            user = form.save()
            
            # Update the user's session to prevent them from being logged out
            update_session_auth_hash(request, user)
            
            # Display a success message
            messages.success(request, 'Your password has been changed successfully.')
            
            return redirect('index')  # Replace 'index' with the desired URL name for the user's profile page
        else:
            # If the form is invalid, display an error message
            messages.error(request, 'Please correct the errors below.')
    else:
        # If the request method is not POST, display an empty form
        form = Pass_word_changeForm(request.user)
    
    context = {'forms': form}
    return render(request, 'change_password.html', context)
