from django.http import JsonResponse
import json
# 导入 Customer
from student.models import student


def dispatcher(request):
    print("进入了dispatcher函数")
    # 将请求参数统一放入request 的 params 属性中，方便后续处理

    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_students':
        print("获取list_students请求")
        return list_students(request)
    elif action == 'add_student':
        return add_student(request)
    elif action == 'modify_student':
        return modify_student(request)
    elif action == 'delete_student':
        return delete_student(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


''' 列出学生信息列表接口数据
{
    "action":"list_students"
}
'''


def list_students(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = student.objects.values()

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    retlist = list(qs)
    print(retlist)
    return JsonResponse({'ret': 0, 'retlist': retlist})


'''接口数据格式
{
    "action":"add_student",
    "data":{
        "accountId":"10080",
        "studentName":"妧同",
        "studentSex":"女",
        "schoolName":"上海吹风大学",
        "studentImage":"url"
    }
}
'''


def add_student(request):
    info = request.params['data']

    # 从请求消息中 获取要添加客户的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    record = student.objects.create(accountId=info['accountId'],
                                    studentName=info['studentName'],
                                    studentSex=info['studentSex'],
                                    schoolName=info['schoolName'],
                                    studentImage=info['studentImage'])

    return JsonResponse({'ret': 0, 'id': record.accountId})


'''
修改学生表信息的接口数据格式
{
    "action":"modify_student",
    "accountId":10080,
    "newdata":{
        "studentName":"王三",
        "studentSex":"男",
        "schoolName":"华丽",
        "studentImage":"url"
    }
}
'''


def modify_student(request):
    # 从请求消息中 获取修改客户的信息
    # 找到该客户，并且进行修改操作

    acId = request.params['accountId']
    newdata = request.params['newdata']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        stu = student.objects.get(accountId=acId)
    except student.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{acId}`的客户不存在'
        }

    if 'studentName' in newdata:
        stu.name = newdata['studentName']
    if 'studentSex' in newdata:
        stu.studentSex = newdata['studentSex']
    if 'schoolName' in newdata:
        stu.schoolName = newdata['schoolName']
    if 'studentImage' in newdata:
        stu.studentImage = newdata['studentImage']
    # 注意，一定要执行save才能将修改信息保存到数据库
    stu.save()

    return JsonResponse({'ret': 0})


''' 删除客户
{
    "action":"del_student",
    "accountId":10080
}
'''


def delete_student(request):
    acId = request.params['accountId']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        stu = student.objects.get(accountId=acId)
    except student.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{acId}`的客户不存在'
        }

    # delete 方法就将该记录从数据库中删除了
    stu.delete()

    return JsonResponse({'ret': 0})
