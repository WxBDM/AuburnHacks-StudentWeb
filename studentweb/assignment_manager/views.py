from django.shortcuts import render
from .models import Assignments

# Create your views here.

def assignmentHTML(request):
    assignment_list = Assignments.objects.all()
    print("assignment list: ")
    for i in assignment_list:
        print(i.name)
    return render(request, "assignment_manager/assignment_manager.html", {'assignments' : assignment_list})
