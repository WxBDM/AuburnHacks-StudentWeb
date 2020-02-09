from django.shortcuts import render
from .models import Assignments

# Create your views here.

def assignmentHTML(request):
    assignment_list = Assignments.objects.all()
    return render(request, "assignment_manager/assignment_manager.html", {'assignments' : assignment_list})

def create_assignment(request):
        if request.method == 'submit':
            if request.POST.get('name') and request.POST.get('duedate'):
                post=Assignments()
                post.name= request.POST.get('name')
                post.due_date= request.POST.get('duedate')
                post.save()
                
                return render(request, 'assignment_manager.html')  

        else:
                print("failed")
                return render(request,'assignment_manager.html')

