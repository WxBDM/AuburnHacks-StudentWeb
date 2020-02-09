from django.contrib import admin
from .models import NewGrade, GradeWeight

# Register your models here.
admin.site.register(NewGrade)
admin.site.register(GradeWeight)