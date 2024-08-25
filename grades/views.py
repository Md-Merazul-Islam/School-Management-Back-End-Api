from rest_framework import viewsets
from .models import Mark
from .serializers import GradeSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = GradeSerializer
