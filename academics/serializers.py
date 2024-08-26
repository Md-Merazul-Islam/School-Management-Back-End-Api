from rest_framework import serializers
from .models import Student, Teacher, Class, Subject
from classes.models import Mark
from classes.serializers import  MarkSerializer

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    marksheet = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = [
            'roll_no', 'username', 'first_name', 'last_name', 'email',
            'phone_number', 'address', 'photo', 'class_name', 'marksheet'
        ]

    def get_marksheet(self, obj):
        marks = Mark.objects.filter(student=obj)
        return MarkSerializer(marks, many=True).data


class TeacherSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.name')

    class Meta:
        model = Teacher
        fields = ['id', 'employee_id', 'first_name', 'last_name', 'email', 'subject_name']
        
        
class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subject
        fields = ['name','slug','code']

