import uuid
from django.db import models
from django.utils.text import slugify


    

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Only slugify the name if the slug is not provided
        super().save(*args, **kwargs)


class Teacher(models.Model):
    username = models.CharField(max_length=100, unique=True ,blank=True,null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50, unique=True, blank=True, editable=False)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.employee_id:
            self.employee_id = self.generate_employee_id()
        super().save(*args, **kwargs)

    def generate_employee_id(self):
        return str(uuid.uuid4().hex[:8].upper())