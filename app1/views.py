from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def samplem(request):
    return HttpResponse('<h1>This is sample m function of app1</h1>')

def samplen(request):
    return HttpResponse('<h1>This is sample n function of app2</h1>')