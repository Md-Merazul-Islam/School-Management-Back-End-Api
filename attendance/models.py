from django.db import models
from django.conf import settings
from classes.models import Class

class Attendance(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])
