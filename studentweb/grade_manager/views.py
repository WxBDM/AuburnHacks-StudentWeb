from django.shortcuts import render

# Create your views here - GRADE MANAGER views

def gradesHTML(request):    
    
    return render(request, "grade_manager/grade_manager.html")