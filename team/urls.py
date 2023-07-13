"""
URL configuration for teamconnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from team import views
from django.urls import path

urlpatterns = [
    path('index/', views.index, name="index"),
    path('addtask/',views.add_task, name="addtask"),
    path('view_task/<int:id>', views.view_task, name="view_task"),
    path('delete_task/<int:id>', views.delete_task, name="delete_task"),
    path('edit_task/<int:id>', views.edit_task, name="edit_task"),
    path('message/', views.Message, name="message"),
    path('register/', views.register, name='register'),
    path('delete_message/<int:id>', views.delete_message, name="delete_message"),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('change-password/', views.change_password, name='change_password'),
]
