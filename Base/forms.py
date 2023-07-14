from django import forms
from .models import User, List, Task

class UserForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ["name", "mail", "password"]
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Nombre completo"
        self.fields['mail'].label = "Contraseña"
        self.fields['password'].label = "Email"

class ListForm(forms.ModelForm):
    class Meta: 
        model = List
        fields = ["title", "description"]

class TaskForm(forms.ModelForm):
    class Meta: 
        model = Task
        fields = ["title", "description", "exp_date", "id_lista"]
    