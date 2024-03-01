from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList, Item

# Create your views here.

def index(response, name):
   todo_list = TodoList.objects.get(name=name)
   items = todo_list.item_set.all()

   items_text = ",</br> ".join([item.text for item in items]);

   return HttpResponse(f"<h1>{todo_list.name}</h1><p>{items_text}</p>")

def v1(response):
   return HttpResponse("<h1>View 1</h1>")
