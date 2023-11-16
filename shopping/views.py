from django.shortcuts import render

# Create your views here.
shop_list=['bread', 'butter', 'cheese']

def index(request):
    return render(request, 'shopping/index.html',{
        'shop_list':shop_list
    })
