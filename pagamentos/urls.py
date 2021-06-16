from django.urls import path
from . import views

urlpatterns = [
    path('process', views.process, name='process'),
    path('sucesso', views.sucesso, name='sucesso')
]
