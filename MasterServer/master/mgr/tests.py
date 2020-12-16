from django.test import TestCase

# Create your tests here.
import requests,pprint

response = requests.get('http://127.0.0.1:8087/api/mgr/students?action=list_students')

pprint.pprint(response.json())

# 添加用户的消息体
stu_add={
    "action":"add_student",
    "data":{
        "accountId":"10080",
        "studentName":"妧同",
        "studentSex":"女",
        "schoolName":"上海吹风大学",
        "studentImage":"https://s3.ax1x.com/2020/12/07/DzZrMn.jpg"
    }
}

response = requests.post('http://127.0.0.1:8087/api/mgr/students',
              json=stu_add)

pprint.pprint(response.json())

