from django.db import models

# Create your models here.
class student(models.Model):
    # 学生账户Id
    accountId = models.CharField(max_length=100)
    # 学生姓名
    studentName = models.CharField(max_length=200)
    # 学生性别
    studentSex = models.CharField(max_length=20)
    # 学校姓名
    schoolName = models.CharField(max_length=200)
    # 用户头像
    studentImage = models.CharField(max_length=400)
    # 自我介绍
    selfIntroduction = models.TextField(max_length=1000, default='')


class School(models.Model):
    # 学校姓名
    schoolName = models.CharField(max_length=200)
    # 学校地址
    schoolAddress = models.CharField(max_length=300)
    # 学校类型
    schoolType = models.CharField(max_length=150)
    # 学校简介
    schoolDescription = models.TextField()
    # 学校logo 用图床存的数据
    schoolLogo = models.CharField(max_length=400)


class HadSendMessage(models.Model):
    # 发送者姓名
    send_name = models.CharField(max_length=100)
    # 学校和年纪
    school_grade = models.CharField(max_length=100)
    # 发送消息
    send_message = models.TextField(max_length=1000)


class Homework(models.Model):
    # 学生姓名
    studentName = models.CharField(max_length=100)
    # 作业名称
    homeworkName = models.CharField(max_length=100)
    # 截至时间
    ddlTime = models.DateTimeField()