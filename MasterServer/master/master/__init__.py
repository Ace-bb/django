import pymysql

pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()

# 创建项目目录
# django-admin startproject bysms
# 启动服务器
# python manage.py runserver 0.0.0.0:8087
# 创建一个APP
# python manage.py startapp sales
# 创建数据库
# python manage.py migrate
# 创建数据库表
# python manage.py makemigrations comm on
# python manage.py migrate
# 创建管理员用户
# python manage.py createsuperuser
# 管理员 134@qq.com   密码 132115abc
# 数据库管理平台
# http://127.0.0.1:8087/admin/
# 搜索调试界面
# http://127.0.0.1:8087/index/index.html
# 课程调试界面
# http://127.0.0.1:8087/course/courses/
# 访问首页
# http://127.0.0.1:8087/index.html
# http://127.0.0.1:8087/index/about.html
# 首页首次进入时自动访问服务器获取全部教师数据get 形式

# http://127.0.0.1:8087/teacher/types?action=get_all_teachers
# 通过选择左侧checkbox后筛选 post方式
''' json格式数据为 
{
    "action":"get_filter_teachers",
    "type":[
        "文学", "理学", "工学", "教授", "四六级" 
    ] 
}
'''
# http://127.0.0.1:8087/teacher/types

# 登录的url
# http://127.0.0.1:8087/login/in
# 账户 132@qq.com  密码 132abc

# 搜索功能
'''  搜索请求的json格式数据 
{ 
    "action":"search",
    "key_word":"工学"
}
'''
# 搜索请求url链接
# http://127.0.0.1:8087/teacher/search
''' 返回的json数据格式
{
    
}

'''
# 获取导师详细信息
# http://127.0.0.1:8087/teacher/detail
''' Json格式数据  POST
{
    "action":"get_teacher_detail_message",
    "id":"10002"
}
'''
'''
{'data': [{'brief_introduction': '2002年毕业于郑州大学化工学院（工学学士），2006年华东理工大学化工学院毕业获工学硕士学位，2010年6月华东理工大学化工学院毕业获工学博士学位。期间在法国国立圣埃蒂安矿业学院进行过为期一年的博士联合培养。',
           'broadcastRoomId': '60002',
           'id': 5,
           'letters': '副教授 硕士生导师',
           'picUrl': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1607834040599&di=8741a9ef5636b5bf340a0ded5c082362&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fq_70%2Cc_zoom%2Cw_640%2Fimages%2F20190314%2F47fccaf9c85447eda76a2a628f485832.jpeg',
           'price': 0.0,
           'rating': 4.9, 
           'schoolName': '上海九龙大学',
           'student_num': 0,
           'teach_type': '工学',
           'teacherId': '10002',
           'teacherName': '孙添越',
           'teacherPosition': '讲师',
           'teacherSex': '男'}],
 'ret': 0} 
'''

# 访问首页about.html
