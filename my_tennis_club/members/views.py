from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

# Create your views here.


# def members(request):
#     my_members = Member.objects.all().values()
#     template = loader.get_template("all_members.html")
#     context = {'my_members': my_members,}
#     return HttpResponse(template.render(context, request))

def testing(request):
    template = loader.get_template("template.html")
    mymembers = Member.objects.all().values()
    mydata = Member.objects.all()
    values_list = Member.objects.values_list('firstname')
    filtered = Member.objects.filter(firstname='jordan100').values()
    filtered_mul = Member.objects.filter(firstname="jordan100").values() | Member.objects.filter(lastname="tejoso100").values()
    filtered_q = Member.objects.filter(Q(firstname="chris100") | Q(lastname="tejoso100")) 
    filtered_char = Member.objects.filter(firstname__startswith="jr").values()
    order_by = Member.objects.all().order_by('firstname').values()
    context = {
        "fruits": ["Apple", "Banana", "Cherry"],
        "name": "jordantanaliga100",
        "lists": mymembers,
        "mymembers": mydata,
        "values_list": values_list,
        "filtered": filtered,
        "filtered_mul": filtered_mul,
        "filtered_q": filtered_q,
        "filtered_char": filtered_char,
        "order_by": order_by,
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
