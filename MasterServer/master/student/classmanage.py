

from django.shortcuts import render

from teacher.models import Teachers, Learn_list
from student.models import student, HadSendMessage, Homework
from course.models import Courses
from django.http import JsonResponse
import json
from django.shortcuts import render

def backHtml(request):
    homeworks = list(Homework.objects.values())
    courses = list(Courses.objects.values())
    return render(request,'classManage.html',{'homeworks':homeworks, 'courses':courses})