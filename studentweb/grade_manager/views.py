from django.shortcuts import render
from django.http import HttpResponse

# Create your views here - GRADE MANAGER views

def gradesHTML(request):    
    return render(request, "grades.html")