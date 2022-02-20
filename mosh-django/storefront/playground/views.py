from django.shortcuts import render
from django.http import HttpResponse

# TODO: View is the handler or the service
# TODO: HERE WE STORE BUSINESS LOGIC

# Create your views here.
# req =>  res

def say_hello(request):
    return render(request, 'index.html', {"name": "Mosh"})
