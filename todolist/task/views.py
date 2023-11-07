from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def helloWorld(request):
    return HttpResponse("Hello Bro, essa é a página inicial da aplicação!")


def taskList(request):
    return render(request, 'task/list.html')


def yourname(request, name):
    return render(request, 'task/yourname.html', {'name': name})
