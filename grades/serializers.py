from rest_framework import serializers
from .models import Mark

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model =Mark
        fields = '__all__'
