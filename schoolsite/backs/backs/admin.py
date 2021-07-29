from django.contrib import admin
from .models import Faculty, Student, Department, Lecturer, Course, StuClass, Studlevel, TimeTable, Time_Table
# Register your models here.
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Lecturer)
admin.site.register(Course)
admin.site.register(StuClass)
admin.site.register(Studlevel)
admin.site.register(Time_Table)
admin.site.register(TimeTable)

