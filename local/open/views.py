from django.shortcuts import render
import datetime
# Create your views here.
from django.http import HttpResponse


def hello_world_view(request):
    return HttpResponse('<h1>hello this is response fron django application</h1>')

def date_time_view(request):
    dete=datetime.datetime.now()
    s='<h1>the current date and time at server is:' + str(datetime)+'</h1>'
    return HttpResponse(s)
