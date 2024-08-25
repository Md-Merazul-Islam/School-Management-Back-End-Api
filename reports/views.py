from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg

from attendance.models import Attendance
from grades.models import Mark
class ReportView(APIView):
    def get(self, request):
        student_id = request.query_params.get('student_id')
        if not student_id:
            return Response({'error': 'Student ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Example: Get average grade for a student
        grades = Mark.objects.filter(student_id=student_id)
        average_grade = grades.aggregate(Avg('grade'))['grade__avg']
        
        # Example: Get attendance for a student
        attendance = Attendance.objects.filter(student_id=student_id)
        total_classes = attendance.count()
        total_present = attendance.filter(status='Present').count()
        
        report = {
            'average_grade': average_grade,
            'total_classes': total_classes,
            'total_present': total_present
        }
        
        return Response(report, status=status.HTTP_200_OK)
