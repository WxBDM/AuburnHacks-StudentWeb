from django.db import models

# Create your models here.

class Class(models.Model):
    instructor_name = models.CharField(max_length = 50)
    instructor_office_hrs = models.CharField(max_length = 20)
    instructor_email = models.CharField(max_length = 40)
    course_name = models.CharField(max_length = 50)
