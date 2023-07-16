from django.urls import path

from .views import home, login, registrar, listaCrear

urlpatterns = [
    path("", home),
    path("login", login),
    path("registrar", registrar),
    path("lista/crear", listaCrear)
]
