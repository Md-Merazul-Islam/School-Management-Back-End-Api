from rest_framework import viewsets
from .models import Teacher,Subject
from .serializers import TeacherSerializer,SubjectSerializer
# from .permissions import IsAdminOrReadOnly 

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes=[IsAdminOrReadOnly]
    
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
