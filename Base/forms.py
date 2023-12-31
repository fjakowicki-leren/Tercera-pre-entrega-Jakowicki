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

class ListCreationForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=50)
    id_user = 0

    def create_list(self):
        cleaned_data = super().clean()
        taskList = List(id_user=self.id_user, description=cleaned_data.get("description"), title=cleaned_data.get("title"))
        taskList.save()

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ListCreationForm, self).__init__(*args, **kwargs)
        self.id_user = user

class TaskCreateForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea(attrs={"maxlength":"500", "cols":False, "rows":"5"}))
    exp_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    id_lista = 0

    def create_task(self):
        cleaned_data = super().clean()
        task = Task(id_lista=self.id_lista, title=cleaned_data.get("title"), description=cleaned_data.get("description"), exp_date=cleaned_data.get("exp_date"))
        task.save()
    
    def __init__(self, *args, **kwargs):
        taskList = kwargs.pop('taskList')
        super(TaskCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Titulo"
        self.fields['description'].label = "Descripción"
        self.fields['exp_date'].label = "Fecha de expiracion"
        self.id_lista = taskList
    