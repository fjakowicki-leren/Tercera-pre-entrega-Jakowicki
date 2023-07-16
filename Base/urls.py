from django.urls import path

from .views import home, login, registrar

urlpatterns = [
    path("", home),
    path("login", login),
    path("registrar", registrar)
]
