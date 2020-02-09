from django.shortcuts import render
from assignment_manager.models import Assignments

# Create your views here.
def overview_page(request):
	assignment_list = Assignments.objects.all()
	return render(request, "overview/class_overview.html", {'assignments' : assignment_list})