from django.urls import path
from . import views

app_name = 'lecture1'
urlpatterns = [
    path('', views.home, name='home page'),
    path('hello/<str:name>', views.hello_name, name='name'),
    path('hello/', views.index, name='index'),
]