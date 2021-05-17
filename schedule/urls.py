from django import urls
from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('tasks',views.tasks,name="tasks")
]