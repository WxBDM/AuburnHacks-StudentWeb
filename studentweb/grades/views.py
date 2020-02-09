from django.shortcuts import render
from django.http import HttpResponse

# Create your views here - GRADES views
def gradesHTML(request):
    return render(request, "static/grades.html")
