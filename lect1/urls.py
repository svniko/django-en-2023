from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home page'),
    path('hello/<str:name>', views.hello_name, name='name'),
    path('hello/', views.hello, name='hello'),
]