from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello, world. You're at the Event index.")


def bonjour(request):
    classe = '5TWIN3'
    return render(request, 'event/hello.html', {'classroom': classe})
