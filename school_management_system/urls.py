from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('accounts.urls')),
    path('attendance/', include('attendance.urls')),
    path('classes/', include('classes.urls')),
    # path('fees/', include('fees.urls')),
    path('grades/', include('grades.urls')),
    path('reports/', include('reports.urls')),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
]
