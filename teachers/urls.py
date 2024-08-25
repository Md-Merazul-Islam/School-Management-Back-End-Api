from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet,SubjectViewSet

router = DefaultRouter()
router.register(r'subjects', TeacherViewSet)
router.register(r'teachers', SubjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
