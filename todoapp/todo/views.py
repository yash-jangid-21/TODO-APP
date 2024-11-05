# Owned by Yash Jangid 
# github_id = yash-jangid-21
# linkeldn_id = yash-21-yash
from django.shortcuts import render,redirect
from todo.models import *


alert = {'flag' :False,
         'role' : '',
         'name' : '' 
         }
priority = ['High','Medium','Low']
def home(request):
    data = Task.objects.all()
    if request.GET.get('search'):
        data = data.filter(task_name__icontains = request.GET.get('search')) 
    return render(request,'home.html',{'data': data,'priority':priority,'alert':alert})

def add(request):
    global alert
    if request.method == "POST":
        alert['role'] = 'success'
        alert['flag'] = True
        alert['name'] = 'Task added Successfully'
        data = request.POST
        Task.objects.create(
            task_name = data.get('taskname'),
            task_priority =data.get('priority'),
            task_duedate =data.get('date')
        )
        return redirect('/')
    return render(request,'add.html')

def delete(request,id):
    global alert
    alert['role'] = 'danger'
    alert['flag'] = True
    alert['name'] = 'Task Delete Successfully'
    Task.objects.get(id=id).delete()
    return redirect('/')

def update(request,id):
    global alert
    alert['role'] = 'info'
    alert['flag'] = True
    alert['name'] = 'Task update Successfully'
    data = Task.objects.get(id=id)
    if request.method == "POST" :
        newdata = request.POST
        data.task_name = newdata.get('taskname')
        data.task_duedate = newdata.get('date')
        data.task_priority =  newdata.get('priority')
        data.save()
        return redirect('/')
    return render(request,'update.html',{'data':data})