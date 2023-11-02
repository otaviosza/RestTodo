from django.db import models

# Create your models here.

class Todolista(models.Model):
    TodolistaId = models.AutoField(primary_key=True)
    TodolistaNome = models.CharField(max_length=100)
    
