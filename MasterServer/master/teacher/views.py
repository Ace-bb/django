from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import json
from teacher.models import Teachers


def dispatcher(request):
    print(request)
    # 将请求参数统一放入request 的 params 属性中，方便后续处理

    # GET请求 参数在url中，同过request 对象的 GET属性获取
    print("!!!!:", request.GET)
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
    if action == 'get_all_teachers':
        print("获取get_all_teachers请求")
        return get_all_teachers(request)
    elif action == 'filter_teacher_type':
        return filter_teacher_type(request)
    elif action == "get_filter_teachers":
        return get_filter_teachers(key_words)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


''' 类型筛选   
{
    "type":""
}
'''


def get_all_teachers(request):
    teachers = Teachers.objects.values()
    reslist = list(teachers)
    # 用session判断登录状态
    loginValue = 0
    userName = request.session.get('username', None)
    print("session: ", request.session)
    print("2:", userName)
    if userName is not None:
        loginValue = 1
    # 返回 loinState = 0 1
    return JsonResponse({'ret': 0, 'loginState': loginValue, 'data': reslist})


def filter_teacher_type(request):
    print("success")
    teachers = Teachers.objects.values()
    # ct = request.GET.get('type', None)
    typeData = request.params['type']
    print(typeData)
    ct = typeData['type']
    print(ct)
    if ct:
        teachers = teachers.filter(teach_type=ct)
    tl = list(teachers)
    print(tl)
    return JsonResponse({'ret': 0, 'teachers': tl})


def get_filter_teachers(key_words):
    typeData = key_words
    print("usertype:", typeData)
    res = []
    for i in range(len(typeData)-1):
        teachers = Teachers.objects.values()
        t = typeData[i]
        if t:
            teachers = teachers.filter(teach_type=t)
        teachers = list(teachers)
        # print(teachers)
        for j in range(len(teachers)):
            res.append(teachers[j])
    print(res)
    return JsonResponse({'ret': 0, 'data': res})
