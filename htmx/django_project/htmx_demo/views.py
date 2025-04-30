from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from datetime import datetime
from django_htmx.http import trigger_client_event

def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})

def get_time(request):
    current_time = datetime.now().strftime("%H:%M:%S")
    return HttpResponse(f"Current time: {current_time}")

def toggle_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.completed = not todo.completed
    todo.save()
    response = HttpResponse(f"""
    <div id="todo-{todo.id}">
        <span>{todo.title}</span>
        <button hx-post="/todo/toggle/{todo.id}" hx-swap="outerHTML" hx-target="closest div">
            {"✅" if todo.completed else "⬜"}
        </button>
    </div>
    """)
    trigger_client_event(response, 'todoToggled', {'id': todo.id, 'completed': todo.completed})
    return response

def add_todo(request):
    title = request.POST.get('title')
    todo = Todo.objects.create(title=title)
    return HttpResponse(f"""
    <div id="todo-{todo.id}">
        <span>{todo.title}</span>
        <button hx-post="/todo/toggle/{todo.id}" hx-swap="outerHTML" hx-target="closest div">⬜</button>
    </div>
    """)
