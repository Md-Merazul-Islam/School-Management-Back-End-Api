from rest_framework import serializers
from .models import Teacher,Subject
from rest_framework.permissions import IsAuthenticated

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
