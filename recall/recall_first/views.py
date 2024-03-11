from django.shortcuts import render, HttpResponse


# Create your views here.
def homefirst(request):
    return HttpResponse('Hello First')
