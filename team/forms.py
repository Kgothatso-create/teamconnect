from django import forms
from .models import AddTask

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = AddTask
        fields = ['task_name', 'assigned_name', 'date_assigned', 'date_due', 'task_details', 'task_importance', 'completion_status']
        widgets = {
            'date_assigned': forms.DateInput(attrs={'type': 'date'}),
            'date_due': forms.DateInput(attrs={'type': 'date'}),
        }
