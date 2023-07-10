from django import forms
from .models import AddTask, Register

class AddTaskForm(forms.ModelForm):
    class Meta:
        # Specify the model associated with the form
        model = AddTask

        # Specify the fields to include in the form
        fields = ['task_name', 'assigned_name', 'date_assigned', 'date_due', 'task_details', 'task_importance', 'completion_status']

        # Define widgets to customize the HTML input types
        widgets = {
            'date_assigned': forms.DateInput(attrs={'type': 'date'}),
            'date_due': forms.DateInput(attrs={'type': 'date'}),
        }

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['username','message']