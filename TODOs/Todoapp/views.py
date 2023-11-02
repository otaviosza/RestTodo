from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from Todoapp.models import Todolista
from Todoapp.serializers import TodolistaSerializer



# Create your views here.


@csrf_exempt
def TodolistaApi(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            todolista = Todolista.objects.all()
            todolist_serializer = TodolistaSerializer(todolista, many=True)
            return JsonResponse(todolist_serializer.data, safe=False)
        else:
            try:
                todolist = Todolista.objects.get(TodolistaId=pk)
                todolist_serializer = TodolistaSerializer(todolist)
                return JsonResponse(todolist_serializer.data, safe=False)
            except Todolista.DoesNotExist:
                return JsonResponse("O cadastro não existe", safe=False)
    
    elif request.method == 'POST':
        todolist_data = JSONParser().parse(request)
        todolist_serializer = TodolistaSerializer(data=todolist_data)
        if todolist_serializer.is_valid():
            todolist_serializer.save()
            return JsonResponse("Cadastro realizado", safe=False)
        return JsonResponse("Não foi cadastrado", safe=False)
    
    elif request.method == 'PUT':
        todolist_data = JSONParser().parse(request)
        try:
            todolist = Todolista.objects.get(TodolistaId=todolist_data['TodolistaId'])
            todolist_serializer = TodolistaSerializer(todolist, data=todolist_data)
            if todolist_serializer.is_valid():
                todolist_serializer.save()
                return JsonResponse("Cadastro Atualizado", safe=False)
            return JsonResponse("Não foi possível atualizar o cadastro", safe=False)
        except Todolista.DoesNotExist:
            return JsonResponse("O cadastro não existe", safe=False)
    
    elif request.method == 'DELETE':
        try:
            todolist = Todolista.objects.get(TodolistaId=pk)
            todolist.delete()
            return JsonResponse("Cadastro deletado com sucesso", safe=False)
        except Todolista.DoesNotExist:
            return JsonResponse("O cadastro não existe", safe=False)

