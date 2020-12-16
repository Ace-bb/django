from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import json
from course.models import Courses


def dispatcher(request):
    print(request)
    # 将请求参数统一放入request 的 params 属性中，方便后续处理

    # GET请求 参数在url中，同过request 对象的 GET属性获取
    print(request.body)
    action = ''
    key_words = []
    if request.method == 'GET':
        request.params = request.GET
        action = request.params['action']

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        action = request.POST.get('action', None)
        key_words = request.POST.get('type', None)
        key_words = key_words.split(',')
        print(key_words)
        # request.params = json.loads(request.body)
        # request.params =request.body
        print(action)

    # 根据不同的action分派给不同的函数进行处理
    # action = request.params['action']
    if action == 'get_all_courses':
        print("获取get_all_teachers请求")
        return get_all_courses(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


''' 类型筛选 
{
    "type":""
}
'''


def get_all_courses(request):
    courses = Courses.objects.values()
    reslist = list(courses)
    return JsonResponse({'ret': 0, 'data': reslist})
