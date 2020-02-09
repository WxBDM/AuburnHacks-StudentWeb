from django.contrib import admin
from .models import NewGrade, GradeWeight, TotalGrade

# Register your models here.
admin.site.register(NewGrade)
admin.site.register(GradeWeight)
admin.site.register(TotalGrade)