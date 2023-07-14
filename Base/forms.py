from django import forms
from .models import User, List, Task

class UserForm(forms.ModelForm):
    class Meta: 
        modal = User
        fields = ["name", "mail", "password"]

class ListForm(forms.ModelForm):
    class Meta: 
        modal = List
        fields = ["title", "description"]

class TaskForm(forms.ModelForm):
    class Meta: 
        modal = Task
        fields = ["title", "description", "exp_date", "id_lista"]