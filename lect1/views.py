from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Django. Lecture1</h1>')

def hello_name(request, name=None):
    flag = True
    # return HttpResponse(f'<h1>Hello, {name.capitalize()}</h1>')
    return render(request, 'lect1/greet.html',{
        'name': name.capitalize(),
        'flag': flag
    })

def hello(request):
    return render(request, 'lect1/index.html')