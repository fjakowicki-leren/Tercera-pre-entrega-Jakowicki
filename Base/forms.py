from django import forms
from .models import User, List, Task

class UserCreateForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ["name", "mail", "password"]
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Nombre completo"
        self.fields['mail'].label = "Email"
        self.fields['password'].label = "Contraseña"

class UserLoginForm(forms.Form):
    mail = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def check(self):
        mail = self.cleaned_data['mail']
        password = self.cleaned_data['password']
        user = User.objects.filter(mail=mail, password=password)
        if user.exists():
            return user[0]
        
        return False
    
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['mail'].label = "Email"
        self.fields['password'].label = "Contraseña"

class ListForm(forms.ModelForm):
    class Meta: 
        model = List
        fields = ["title", "description"]

class TaskForm(forms.ModelForm):
    class Meta: 
        model = Task
        fields = ["title", "description", "exp_date", "id_lista"]
    