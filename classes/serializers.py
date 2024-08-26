from rest_framework import serializers
from .models import Attendance, Mark

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class MarkSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.name')
    
    class Meta:
        model = Mark
        fields = ['subject_name', 'grade', 'marks']
