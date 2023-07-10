from django import forms
from .models import AddTask, Register
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AddTaskForm(forms.ModelForm):
    class Meta:
        # Specify the model associated with the form
        model = AddTask

        # Specify the fields to include in the form
        fields = ['task_name', 'assigned_name', 'date_assigned', 'date_due', 'task_details', 'task_importance', 'completion_status']

        # Define widgets to customize the HTML input types
        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'form-control'}),
            'assigned_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_assigned': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_due': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'task_details': forms.Textarea(attrs={'class': 'form-control'}),
            'task_importance': forms.Select(attrs={'class': 'form-control'}),
            'completion_status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class RegisterForm(forms.ModelForm):
    # username field with a maximum length of 50 characters
    # and widget attributes for autofocus and CSS class
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))

    # message field with a maximum length of 550 characters
    # and widget attributes for autofocus, CSS class, and initial value
    message = forms.CharField(max_length=550, widget=forms.Textarea(attrs={'autofocus': 'True', 'class': 'form-control'}), initial='')

    class Meta:
        # specify the model that this form is associated with
        model = Register

        # specify the fields from the model that should be included in the form
        fields = ['username', 'message']


class RegistrationForm(UserCreationForm):
    # username field with widget attributes for autofocus and CSS class
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    
    # email field with widget attributes for CSS class
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    # password1 field with label and widget attributes for CSS class
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    # password2 field with label and widget attributes for CSS class
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        # specify the model that this form is associated with
        model = User
        
        # specify the fields from the model that should be included in the form
        fields = ['username', 'password1', 'password2', 'email']