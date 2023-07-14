from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import UserForm

def registrar(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()
    return render(request, "registrar.html", {"form": form})