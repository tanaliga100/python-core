from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoList, Item
from .forms import CreateNewList

# Create your views here.

def home(request):
    context = {"home": "This is Home Page"}
    return render(request, "main/home.html", context)


def about(request):
    context = {"about": "This is About Page"}
    return render(request, "main/about.html", context)


def lists(request, id):
    todo_list = TodoList.objects.get(id=id)
    print(todo_list)
    items = todo_list.item_set.all()
    items_text = ",</br> ".join([item.text for item in items])

    context = {
        "list_name": todo_list.name,
        "items_text": items_text
    }
    #  return HttpResponse(f"<h1>{todo_lst.iname}</h1><p>{items_text}</p>")
    return render(request, "main/lists.html", {"lists": todo_list})


def create(request):
    if request.method == "POST":
      form = CreateNewList(request.POST)  
      if form.is_valid():
        n = form.cleaned_data['title']
        t = TodoList(name=n)
        t.save()
        
      return HttpResponseRedirect("/%i" %t.id)
      
    else:
      form = CreateNewList()
    return render(request, "main/create.html", {"forms": form})
