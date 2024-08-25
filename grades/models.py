from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from classes.models import Class
from teachers.models import Subject

class Mark(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, blank=True, null=True)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    marks = models.PositiveIntegerField()
    grade = models.CharField(max_length=2, blank=True, null=True, editable=False)

    class Meta:
        unique_together = ('student', 'subject')

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.marks} - {self.grade}"

    def save(self, *args, **kwargs):
        if self.marks is not None:
            self.grade = self.determine_grade(self.marks)
        super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        if self.marks is not None:
            if self.marks < 0 or self.marks > 100:
                raise ValidationError("Marks must be between 0 and 100.")

    def determine_grade(self, marks):
        if marks >= 90:
            return 'A+'
        elif marks >= 80:
            return 'A'
        elif marks >= 70:
            return 'B+'
        elif marks >= 60:
            return 'B'
        elif marks >= 50:
            return 'C+'
        elif marks >= 40:
            return 'C'
        else:
            return 'F'
