from django.shortcuts import render
from django.http import HttpResponse 
from schedule.models import Task

# Create your views here.
def home(request):
    context = {'success': False ,'name': 'Abhishek'}
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        ins = Task(tasktitle = title, taskdescription = description)
        ins.save()
        context = {'success': True}
    
    return render(request,'home.html', context)

def tasks(request):
    alltasks = Task.objects.all()
    context = {'tasks':alltasks}
    return render(request,'tasks.html', context)
