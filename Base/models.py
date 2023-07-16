from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    mail = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return "User " + self.name

class List(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    id_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False) 

    def __str__(self):
        return "Lista " + self.title

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    exp_date = models.DateField(null=True)
    id_lista = models.ForeignKey(List, on_delete=models.SET_NULL, null=True, blank=False) 
    
    def __str__(self):
        return "Tarea " + self.title
   