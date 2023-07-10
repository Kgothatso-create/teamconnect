from django.db import models
from datetime import date


# Create your models here.
class AddTask(models.Model):
    # The primary key for the task
    id = models.AutoField(primary_key=True)

    # The name of the task (maximum length: 50 characters)
    task_name = models.CharField(max_length=50)

    # The name of the person assigned to the task (maximum length: 50 characters)
    assigned_name = models.CharField(max_length=50)

    # The date the task was assigned (default value: today's date)
    date_assigned = models.DateField(default=date.today)

    # The due date of the task
    date_due = models.DateField()

    # Additional details about the task
    task_details = models.TextField()

    # The importance level of the task (choices: low, medium, high)
    task_importance = models.CharField(max_length=10, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])

    # The completion status of the task (choices: incomplete, complete)
    completion_status = models.CharField(max_length=10, choices=[('incomplete', 'Incomplete'), ('complete', 'Complete')])

    def __str__(self):
        # Returns a string representation of the task, including its ID and name
        return f"ID: {self.id} - {self.task_name}"
    
class Register(models.Model):
    id = models.AutoField(primary_key=True)
    # Auto-incrementing primary key field
    
    username = models.CharField(max_length=50)
    # CharField for storing the username
    
    message = models.TextField(max_length=550, default="")
    # TextField for storing the message with a default value of an empty string
    
    def __str__(self):
        # Define a string representation for the Register object
        return f"id:{self.id} - username:{self.username}"

    