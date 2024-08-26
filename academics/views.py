from rest_framework import viewsets
from .models import Student, Teacher, Class, Subject
from .serializers import StudentSerializer, TeacherSerializer, ClassSerializer, SubjectSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


from rest_framework import generics
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

class StudentFilter(filters.FilterSet):
    username = filters.CharFilter(field_name='username', lookup_expr='icontains')
    roll_no = filters.NumberFilter(field_name='roll_no')

    class Meta:
        model = Student
        fields = ['username', 'roll_no']
        
        
class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter
    
    
    
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Teacher
from .serializers import TeacherSerializer
from .filters import TeacherFilter

class TeacherListView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TeacherFilter
    
    
    
    
    
from rest_framework import generics
from rest_framework.response import Response
from django_filters import rest_framework as filters
from .models import Teacher
from .serializers import TeacherSerializer

class TeacherFilter(filters.FilterSet):
    email = filters.CharFilter(field_name='email', lookup_expr='icontains')
    subject = filters.NumberFilter(field_name='subject')
    employee_id = filters.NumberFilter(field_name='employee_id')

    class Meta:
        model = Teacher
        fields = ['employee_id', 'email', 'subject']
