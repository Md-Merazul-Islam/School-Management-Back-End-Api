from django.db import models
from academics.models import Student, Subject


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    grade = models.CharField(max_length=2, editable=False)

    def save(self, *args, **kwargs):
        self.grade = self.calculate_grade(self.marks)
        super().save(*args, **kwargs)

    def calculate_grade(self, marks):
        if marks >= 90: return 'A+'
        elif marks >= 80: return 'A'
        elif marks >= 70: return 'B+'
        elif marks >= 60: return 'B'
        elif marks >= 50: return 'C+'
        elif marks >= 40: return 'C'
        else: return 'F'

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.grade}"

