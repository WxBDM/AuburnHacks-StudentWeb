from django.shortcuts import render
from .models import NewGrade, GradeWeight, TotalGrade

# Create your views here - GRADE MANAGER views

def gradesHTML(request):    
	grades = NewGrade.objects.all()
	weights = GradeWeight.objects.all()
	total = TotalGrade.objects.all()

	# calculate 
	for i, grade in enumerate(grades):
		perc = float(grade.recieved_grade) / float(grade.total_points)
		grades[i].percentage = int(perc * 100)	

	return render(request, "grade_manager/grade_manager.html", {'grades' : grades, 'weights' : weights, 'final_grade' : total})