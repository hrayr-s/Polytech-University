from django.contrib import admin

from university.models import Student, Group, Profession, Faculty, Staff, Department, WorkerType, Subject, ExamType

admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Profession)
admin.site.register(Faculty)
admin.site.register(Subject)
admin.site.register(Staff)
admin.site.register(Department)
admin.site.register(WorkerType)
admin.site.register(ExamType)