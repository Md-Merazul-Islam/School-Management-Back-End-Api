from django_filters import rest_framework as filters
from .models import Teacher

class TeacherFilter(filters.FilterSet):
    email = filters.CharFilter(field_name='email', lookup_expr='icontains')
    subject = filters.NumberFilter(field_name='subject')
    employee_id = filters.NumberFilter(field_name='employee_id')

    class Meta:
        model = Teacher
        fields = ['employee_id', 'email', 'subject']
