from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList, Item

# Create your views here.


def home(response):
    context = {"home": "This is Home Page"}
    return render(response, "main/home.html", context)

def lists(response, id):
    todo_list = TodoList.objects.get(id=id)
    print(todo_list)
    items = todo_list.item_set.all()
    items_text = ",</br> ".join([item.text for item in items])

    context = {
        "list_name": todo_list.name,
        "items_text": items_text
    }
    #  return HttpResponse(f"<h1>{todo_lst.iname}</h1><p>{items_text}</p>")
    return render(response, "main/lists.html", {"lists": todo_list})


def about(response):
    context = {"about": "This is About Page"}
    return render(response, "main/about.html", context)
