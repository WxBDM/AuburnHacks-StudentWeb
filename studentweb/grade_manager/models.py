from django.db import models

# Create your models here.

class GradeWeight(models.Model):
    weight1 = models.IntegerField()
    weight2 = models.IntegerField()
    weight3 = models.IntegerField()
    weight4 = models.IntegerField()
    weight5 = models.IntegerField()

class NewGrade(models.Model):
	assignment_name = models.CharField(max_length = 30)
	assignment_category = models.CharField(max_length = 30)
	recieved_grade = models.IntegerField()
	total_points = models.IntegerField()
	percentage = models.IntegerField()

class TotalGrade(models.Model):
	total = models.IntegerField()