from django.contrib import admin
from .models import Attendance, Mark

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status')
    search_fields = ('student__first_name', 'student__last_name', 'date')
    list_filter = ('status', 'date')
    ordering = ('-date',)

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'marks', 'grade')
    search_fields = ('student__first_name', 'student__last_name', 'subject__name')
    list_filter = ('subject', 'grade')
    ordering = ('student', 'subject')
