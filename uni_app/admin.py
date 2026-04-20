from django.contrib import admin
from .models import Student, StudentAusweis, Professor, Semester, Kursbeschreibung, Kurs

# Register your models here.

admin.site.register(Student)
admin.site.register(StudentAusweis)
admin.site.register(Professor)
admin.site.register(Semester)
admin.site.register(Kursbeschreibung)
admin.site.register(Kurs)