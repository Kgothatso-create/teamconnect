from django.db import models
from datetime import date

# Create your models here.
class AddTask(models.Model):
    id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=50)
    assigned_name = models.CharField(max_length=50)
    date_assigned = models.DateField(default=date.today)
    date_due = models.DateField()
    task_details = models.TextField()
    task_importance = models.CharField(max_length=10, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    completion_status = models.CharField(max_length=10, choices=[('incomplete', 'Incomplete'), ('complete', 'Complete')])

    def __str__(self):
        return f"ID: {self.id} - {self.task_name}"