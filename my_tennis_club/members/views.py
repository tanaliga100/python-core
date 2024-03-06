from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.


# def members(request):
#     my_members = Member.objects.all().values()
#     template = loader.get_template("all_members.html")
#     context = {'my_members': my_members,}
#     return HttpResponse(template.render(context, request))

def testing(request):
  template = loader.get_template("template.html")
  mymembers = Member.objects.all().values()
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
    'name': "jordantanaliga100",
    'lists': mymembers
  }
  return HttpResponse(template.render(context, request))

def main(request): 
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        "mymembers": mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id): 
    mymember = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
      'mymember': mymember,
    } 
    return HttpResponse(template.render(context, request))
   
