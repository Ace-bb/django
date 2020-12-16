from django.shortcuts import render

# Create your views here.
# 导入 Customer 对象定义
from django.http import HttpResponse
from course.models import Courses

# 先定义好HTML模板
html_template = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
table {
    border-collapse: collapse;
}
th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
</style>
</head>
    <body> 
        
        <table>
        <tr>
        <th>id</th>
        <th>课程编号</th>
        <th>课程名称</th>
        <th>导师名称</th>
        <th>上课时间</th>
        <th>课程标签</th>
        <th>学生人数</th>
        </tr>

        %s


        </table>
    </body>
</html>
'''
def listorders(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    # 每条表记录都是是一个dict对象，
    # key 是字段名，value 是 字段值
    qs = Courses.objects.values()
    # 检查url中是否有参数phonenumber
    print(request)
    oi = request.GET.get('condition',None)

    # 如果有，添加过滤条件
    if oi:
        qs = qs.filter(courseName=oi)

    # 定义返回字符串
    retStr = ''
    for orders in  qs:
        retStr += '<tr>'
        for name, value in orders.items():
            retStr += f'<td>{value} </td> '

        # <br> 表示换行
        retStr += '</tr>'

    return HttpResponse(html_template%retStr)