from django.db import models
from classes.models import Class
from grades.models import Mark

class Student(models.Model):
    roll_no = models.IntegerField(unique=True, editable=False, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True, unique=True) 
    email = models.EmailField(unique=True, blank=True, null=True)
    date_of_birth = models.DateField()
    address = models.TextField()
    class_name = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    gpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True ,editable=False)

    def save(self, *args, **kwargs):
        if not self.roll_no:
            last_student = Student.objects.order_by('-roll_no').first()
            if last_student:
                self.roll_no = last_student.roll_no + 1
            else:
                self.roll_no = 5000
        self.gpa = self.calculate_gpa()
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return (f" {self.roll_no}, ----"
                f"{self.first_name} {self.last_name},--- "
                f"GPA: {self.gpa}---")

    def calculate_gpa(self):
        marks = Mark.objects.filter(student=self)

        if not marks.exists():
            return None

        total_points = 0
        total_subjects = 0

        for mark in marks:
            grade_value = self.get_grade_value(mark.grade)
            if grade_value is not None:
                if grade_value == 0.0:  # If any subject has an 'F', return GPA as 0.0
                    return 0.0
                total_points += grade_value
                total_subjects += 1

        if total_subjects == 0:
            return None

        gpa = total_points / total_subjects
        return round(gpa, 2)

    def get_grade_value(self, grade):
        grade_values = {
            'A+': 4.0,
            'A': 3.7,
            'B+': 3.3,
            'B': 3.0,
            'C+': 2.7,
            'C': 2.0,
            'D': 1.0,
            'F': 0.0,
        }
        return grade_values.get(grade.upper(), None)






from django.db import models
from students.models import Student
from classes.models import Class
from teachers.models import Subject

class MarkSheet(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='mark_sheet')
    class_name = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    total_gpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - Total GPA: {self.total_gpa}"

    def calculate_total_gpa(self):
        marks = self.student.marks_set.all()
        total_points = 0
        total_subjects = 0

        for mark in marks:
            grade_value = self.student.get_grade_value(mark.grade)
            if grade_value is not None:
                total_points += grade_value
                total_subjects += 1

            # If the student has an F grade in any subject, total GPA should be 0.0
            if mark.grade == 'F':
                self.total_gpa = 0.0
                return

        if total_subjects > 0:
            self.total_gpa = round(total_points / total_subjects, 2)
        else:
            self.total_gpa = None

    def save(self, *args, **kwargs):
        self.calculate_total_gpa()
        super().save(*args, **kwargs)

class MarkDetail(models.Model):
    mark_sheet = models.ForeignKey(MarkSheet, on_delete=models.CASCADE, related_name='marks_details')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    grade = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return f"{self.mark_sheet.student} - {self.subject} - {self.marks} - {self.grade}"

    def save(self, *args, **kwargs):
        if self.marks is not None:
            self.grade = self.mark_sheet.student.get_grade_value(self.marks)
        super().save(*args, **kwargs)
