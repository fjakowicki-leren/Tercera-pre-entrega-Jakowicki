from django.urls import path

from .views import registrar

urlpatterns = [
    path("", registrar)
]
