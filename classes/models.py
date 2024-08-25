from django.db import models
from teachers.models import Teacher

class Class(models.Model):
    SECTIONS = [
        ('A', 'Section A'),
        ('B', 'Section B'),
        ('C', 'Section C'),
        ('D', 'Section D'),
        ('E', 'Section E'),
    ]

    name = models.CharField(max_length=100)
    # teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    # students = models.ManyToManyField('students.Student')
    section = models.CharField(max_length=1, choices=SECTIONS, default='A')

    def __str__(self):
        return f"{self.name} - {self.get_section_display()}"
