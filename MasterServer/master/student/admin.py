from django.contrib import admin

# Register your models here.
from .models import student,School, Homework
# Register your models here.
admin.site.register(student)
admin.site.register(School)
admin.site.register(Homework)