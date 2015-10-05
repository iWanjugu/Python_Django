from django.contrib import admin
from .models import Student, Classroom
from .forms import StudentForm
# Register your models here.

class StudentAdmin (admin.ModelAdmin):
    form = StudentForm


#Registering a class
admin.site.register(Student, StudentAdmin)
admin.site.register(Classroom)


#register forms


