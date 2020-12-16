from django.db import models

# Create your models here.
# Create your models here.
class Courses(models.Model):
    # 课程编号
    courseId=models.CharField(max_length=200)
    # 课程名称
    courseName=models.CharField(max_length=200)
    # 导师名称
    teacherName=models.CharField(max_length=200)
    # 上课时间
    classTime = models.DateTimeField()
    # 课程标签
    courseLable=models.CharField(max_length=200)
    # 学生数量
    studentNum=models.IntegerField()
    # 课程图片
    coursePic = models.CharField(max_length=500, default='http://')
    # 课程评分
    courseRate = models.FloatField(default=0.0)
    # 课程价格
    coursePrice = models.FloatField(default=0.0)

