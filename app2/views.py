from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<h1>This is first function of app2</h1>')


def second(request):
    return HttpResponse('<h1>This is second function of app2</h1>')