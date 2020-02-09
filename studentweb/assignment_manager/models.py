from django.db import models

# Create your models here.
class Assignments(models.Model):
    name = models.CharField(max_length = 50)
    due_date = models.CharField(max_length = 5)
    