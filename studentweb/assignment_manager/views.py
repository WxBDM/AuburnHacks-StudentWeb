from django.shortcuts import render

# Create your views here.

def assignmentHTML(request):
	return render(request, "assignment_manager/assignment_manager.html")
