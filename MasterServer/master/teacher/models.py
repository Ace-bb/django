from django.db import models


# Create your models here.
class Teachers(models.Model):
    # 导师ID
    teacherId = models.CharField(max_length=200)
    # 导师姓名
    teacherName = models.CharField(max_length=100)
    # 导师性别
    teacherSex = models.CharField(max_length=20)
    # 导师地址
    teacherPosition = models.CharField(max_length=300)
    # 导师学校
    schoolName = models.CharField(max_length=100)
    # 直播房间号
    broadcastRoomId = models.CharField(max_length=100)
    # 主研方向
    teach_type = models.CharField(max_length=100)
    # 导师图片
    picUrl = models.CharField(max_length=500, default='http://')
    # 导师评分
    rating = models.FloatField(default=5.0)
    # 导师简介
    brief_introduction = models.TextField(max_length=200, default=None)
    # 导师寄语
    letters = models.CharField(max_length=200, default=None)
    # 学生数
    student_num = models.IntegerField(default=0)
    # 价格
    price = models.FloatField(default=0.0)
    # 头像
    icon = models.CharField(max_length=500, default='https://')

class Learn_list(models.Model):
    # 导师ID
    teacherId = models.CharField(max_length=200)
    # 导师姓名
    teacherName = models.CharField(max_length=100)
    # 老师将教学的内容
    you_can_learn = models.CharField(max_length=100)


