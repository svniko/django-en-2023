from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

class NewItemForm(forms.Form):
    item = forms.CharField(label='New Item')

# Create your views here.
# shop_list=['bread', 'butter', 'cheese']

def index(request):
    if 'shop_list' not in request.session:
        request.session['shop_list'] = []
    return render(request, 'shopping/index.html',{
        # 'shop_list':shop_list
        'shop_list':request.session['shop_list']
    })

# def add(request):
#     if request.method == "POST":
#         item = request.POST.get('item')
#         shop_list.append(item)
#     return render(request, 'shopping/add.html')

def add(request):
    if request.method == "POST":
        form = NewItemForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data['item']
            # shop_list.append(item)
            request.session['shop_list'] += [item]
            return HttpResponseRedirect(reverse("shopping:index"))
    return render(request, 'shopping/add.html',{
        "form": NewItemForm()
    })