from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import UserCreateForm, UserLoginForm
from .models import List, Task, User

def login(request: HttpRequest) -> HttpResponse:
    usuario_creado = request.session.get('usuario_creado')
    if usuario_creado:
        return redirect(home)
    else:
        err = False
        
        if request.method == "POST":
            form = UserLoginForm(request.POST)
            print(form)
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
    print("home")
    if usuario_creado:
        lists = False
        id_user = User.objects.filter(mail=usuario_creado['correo'])
        
        if id_user.exists:
            id_user = id_user[0].id
            lists = List.objects.filter(id_user=id_user)
            if lists.exists():
                lists = lists[0]

        return render(request, "home.html", {'usuario': usuario_creado, 'listas': lists})
    else:
        return redirect(login)
    