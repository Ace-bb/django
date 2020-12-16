from django.shortcuts import render

from teacher.models import Teachers, Learn_list
from student.models import student, HadSendMessage
from django.http import JsonResponse
import json
from django.shortcuts import render


# Create your views here.

def sendMesHtml(request):
    if request.method == 'GET':
        request.params = request.GET
        id = request.params['teacherId']

    teachers = list(Teachers.objects.values().filter(teacherId=id))
    info_dict = {'teacherName': teachers[0]['teacherName'], 'picUrl': teachers[0]['picUrl'],
                 'letters': teachers[0]['letters']}
    studentList = list(student.objects.values())
    students = studentList[0]['studentName']
    print(students)
    return render(request, 'SendRequest.html', {'teachers': info_dict, 'students': students})


def sendMes(request):
    print("sendMes:", request.POST)
    message = request.POST.get('message', None)
    name = request.POST.get('name', None)
    grade = request.POST.get('grade', None)
    record = HadSendMessage.objects.create(send_name=name,
                                           school_grade=grade,
                                           send_message=message)
    return JsonResponse({'ret': 0, 'id': record.id})
