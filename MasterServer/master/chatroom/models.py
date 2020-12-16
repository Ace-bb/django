from django.db import models


# Create your models here.
class ChatRoom(models.Model):
    # 聊天室ID
    chatRoomId = models.CharField(max_length=100)
    # 学生Id
    studentId = models.CharField(max_length=100)
    # 导师ID
    teacherId = models.CharField(max_length=100)
    # 聊天时间
    chatRoomTime = models.DateTimeField()


# 聊天记录的表
class ChatRecord(models.Model):
    # 聊天记录编号ID
    recordId = models.CharField(max_length=100)
    # 发送时间
    sendTime = models.DateTimeField()
    # 发送者
    sendName = models.CharField(max_length=100)
    # 接收者
    receiveName = models.CharField(max_length=100)
    # 内容
    message = models.TextField()


class ChatHistroy(models.Model):
    # 学生ID
    studentId = models.CharField(max_length=100)
    # 学生姓名
    studentName = models.CharField(max_length=100)
    # 老师姓名
    taecherName = models.CharField(max_length=100)
    # 老师头像
    teacherIcon = models.CharField(max_length=500)
    # 最近一条消息
    lastMessage = models.CharField(max_length=200)
