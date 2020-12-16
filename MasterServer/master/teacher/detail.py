from django.http import JsonResponse
from teacher.models import Teachers, Learn_list
import json
from django.shortcuts import render


def viewHtml(request):
    info_dict = {'teacherName': '王三', 'fromSchool': '华东吹风大学', 'studentLevel': '初学者', 'studentNumber': '8542',
                 'teachTime': '01h 30m', 'courseNum': '21'}

    learn = []
    if Learn_list.objects.values().filter(teacherId='10002'):
        learn = list(Learn_list.objects.values().filter(teacherId='10002'))
    print(learn)
    first = []
    for i in range(len(learn) - 3):
        first.append(learn[i]['you_can_learn'])
    second = []
    for i in range(3, len(learn)):
        second.append(learn[i]['you_can_learn'])
    learnList = {'first': first, 'second': second}

    teachers = list(Teachers.objects.values().filter(teacherId = '10002'))
    teacherIntro = teachers[0]['brief_introduction']
    teacherId = teachers[0]['teacherId']
    info_dict = {'teacherName': teachers[0]['teacherName'], 'fromSchool': teachers[0]['schoolName'], 'studentLevel': '初学者',
                 'studentNumber': teachers[0]['student_num'], 'teachTime': '01h 30m', 'courseNum': '21'}
    return render(request, 'course_view.html', {'info': info_dict, 'learnList': learnList, 'teacherIntro': teacherIntro,
                                                'teacherId': teacherId})
