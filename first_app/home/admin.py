from django.contrib import admin
from .models import Student, Classroom
# from .models import Classroom


# Register your models here.

#Registering a class
admin.site.register(Student)


# register class room
admin.site.register(Classroom)

