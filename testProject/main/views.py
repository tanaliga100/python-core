from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList, Item

# Create your views here.

def index(response, id):
   todo_list = TodoList.objects.get(id=id)
  #  items = todo_list.item_set.all()
  #  items_text = ",</br> ".join([item.text for item in items]);
  
   return render(response, "main/base.html", {"name": todo_list.name})
  #  return HttpResponse(f"<h1>{todo_list.name}</h1><p>{items_text}</p>")

def home(response):
   return render(response, "main/home.html", {"name": "test"})

