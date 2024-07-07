from django.shortcuts import render
import requests

API_URL_BASE = 'http://localhost:8000/api/todos/'

def home(request):
    return render(request, 'home.html')

def todos_ids(request):
    response = requests.get(f'{API_URL_BASE}ids/')
    todos = response.json()
    return render(request, 'todos_list.html', {'todos': todos, 'type': 'IDs'})

def todos_ids_titles(request):
    response = requests.get(f'{API_URL_BASE}ids_titles/')
    todos = response.json()
    return render(request, 'todos_list.html', {'todos': todos, 'type': 'IDs and Titles'})

def todos_unresolved(request):
    response = requests.get(f'{API_URL_BASE}unresolved/')
    todos = response.json()
    return render(request, 'todos_list.html', {'todos': todos, 'type': 'Unresolved'})

def todos_resolved(request):
    response = requests.get(f'{API_URL_BASE}resolved/')
    todos = response.json()
    return render(request, 'todos_list.html', {'todos': todos, 'type': 'Resolved'})

def todos_ids_userids(request):
    response = requests.get(f'{API_URL_BASE}ids_userids/')
    todos = response.json()
    return render(request, 'todos_list.html', {'todos': todos, 'type': 'IDs and UserIDs'})

def todos_resolved_userids(request):
    response = requests.get(f'{API_URL_BASE}resolved_userids/')
    todos = response.json()
    return render(request, 'todos_list.html', {'todos': todos, 'type': 'Resolved UserIDs'})

def todos_unresolved_userids(request):
    response = requests.get(f'{API_URL_BASE}unresolved_userids/')
    todos = response.json()
    return render(request, 'todos_list.html', {'todos': todos, 'type': 'Unresolved UserIDs'})
