from django.http import JsonResponse
from teacher.models import Teachers
import json


# 搜索导师表
def search_all(request):
    print(request.POST)
    teacher_list = []
    key_word = request.POST.get('key_word', None)
    print(key_word)
    if Teachers.objects.values().filter(teacherName=key_word):
        teacher_list.append(list(Teachers.objects.values().filter(teacherName=key_word)))
    if Teachers.objects.values().filter(teacherPosition=key_word):
        teacher_list.append(list(Teachers.objects.values().filter(teacherPosition=key_word)))
    if Teachers.objects.values().filter(schoolName=key_word):
        teacher_list.append(list(Teachers.objects.values().filter(schoolName=key_word)))
    print(teacher_list)
    if Teachers.objects.values().filter(teach_type=key_word):
        teacher_list.append(list(Teachers.objects.values().filter(teach_type=key_word)))
    print(teacher_list)
    return JsonResponse({'ret': 0, 'data': teacher_list[0]})


def get_detail(request):
    print(json.loads(request.body))
    print(request.POST)
    teacher_message = []
    request.params = json.loads(request.body)
    teacher_name = request.POST.get('name', None)
    teacher_id = request.POST.get('id', None)
    if teacher_id is None:
        teacher_id = request.params['id']
    print(teacher_id)
    if Teachers.objects.values().filter(teacherId=teacher_id):
        teacher_message = list(Teachers.objects.values().filter(teacherId=teacher_id))
    return JsonResponse({'ret': 0, 'data': teacher_message})
