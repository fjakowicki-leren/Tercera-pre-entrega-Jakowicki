from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import UserCreateForm, UserLoginForm, ListCreationForm, TaskCreateForm
from .models import List, Task, User

def login(request: HttpRequest) -> HttpResponse:
    usuario_creado = request.session.get('usuario_creado')
    if usuario_creado:
        return redirect(home)
    else:
        err = False
        
        if request.method == "POST":
            form = UserLoginForm(request.POST)
            if form.is_valid():
                user = form.check()
                if user:
                    usuario_creado = {'nombre': user.name, 'correo': user.mail}
                    request.session['usuario_creado'] = usuario_creado  
                    return redirect(home)
                else:
                    err = "No existe el usuario"
        else:
            form = UserLoginForm()

        return render(request, "login.html", {"form": form, "error": err})

def registrar(request: HttpRequest) -> HttpResponse:
    err = False

    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            usuario_creado = {'nombre': form.cleaned_data['name'], 'correo': form.cleaned_data['mail']}
            request.session['usuario_creado'] = usuario_creado
            form.save()
            return redirect(home)
        else:
            err = "Los valores ingresados no son validos"
    else:
        form = UserCreateForm()

    return render(request, "registrar.html", {"form": form, "error": err})

def home(request: HttpRequest) -> HttpResponse:
    usuario_creado = request.session.get('usuario_creado')
    if usuario_creado:
        lists = False
        id_user = User.objects.filter(mail=usuario_creado['correo'])
        
        if id_user.exists():
            id_user = id_user[0].id
            
            lists = list(List.objects.filter(id_user=id_user))
        print(lists)
        return render(request, "home.html", {'usuario': usuario_creado, 'listas': lists})
    else:
        return redirect(login)
    
def lista(request: HttpRequest, id) -> HttpResponse:
    usuario_creado = request.session.get('usuario_creado')
    if usuario_creado:
        taskList = List.objects.filter(id=id)
        
        if taskList.exists():
            taskList = taskList[0]
        else:
            return redirect(home)
        
        tasks = list(Task.objects.filter(id_lista=taskList.id))

        err = False

        if request.method == "POST":
            form = TaskCreateForm(request.POST, taskList=taskList)
            if form.is_valid():
                form.create_task()
                return redirect(lista, id)
            else:
                err = "Los campos no son validos"
        else:
            form = TaskCreateForm(taskList=taskList)

        return render(request, "lista.html", {"tasks": tasks, "list": taskList, "form": form, "error": err})
    else:
        return redirect(login)     
    
def listaCrear(request: HttpRequest) -> HttpResponse:
    usuario_creado = request.session.get('usuario_creado')
    user = User.objects.filter(mail=usuario_creado['correo'])

    if user.exists():
        user = user[0]

        err = False

        if request.method == "POST":
            form = ListCreationForm(request.POST, user=user)
            if form.is_valid():
                form.create_list()
                return redirect(home)
            else:
                err = "Los campos no son validos"
        else:
            form = ListCreationForm(user=user)

        return render(request, "creacionLista.html", {"form": form, "error": err})
    else:
        if usuario_creado:
            del request.session['usuario_creado']
            request.session.modified = True
        return redirect(login)     
    