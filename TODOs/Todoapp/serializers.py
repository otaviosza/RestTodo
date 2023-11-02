from rest_framework import serializers
from Todoapp.models import Todolista

class TodolistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolista
        fields = ('TodolistaId',
                  'TodolistaNome')