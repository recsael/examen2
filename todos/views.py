from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class TodoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

@api_view(['GET'])
def todo_ids(request):
    ids = Todo.objects.values_list('id', flat=True)
    return Response(ids)

@api_view(['GET'])
def todo_ids_titles(request):
    todos = Todo.objects.values('id', 'title')
    return Response(todos)

@api_view(['GET'])
def todo_unresolved(request):
    todos = Todo.objects.filter(is_done=False).values('id', 'title')
    return Response(todos)

@api_view(['GET'])
def todo_resolved(request):
    todos = Todo.objects.filter(is_done=True).values('id', 'title')
    return Response(todos)

@api_view(['GET'])
def todo_ids_userids(request):
    todos = Todo.objects.values('id', 'user_id')
    return Response(todos)

@api_view(['GET'])
def todo_resolved_userids(request):
    todos = Todo.objects.filter(is_done=True).values('id', 'user_id')
    return Response(todos)

@api_view(['GET'])
def todo_unresolved_userids(request):
    todos = Todo.objects.filter(is_done=False).values('id', 'user_id')
    return Response(todos)