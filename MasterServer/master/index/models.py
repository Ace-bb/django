from django.db import models

# Create your models here.
class Schools(models.Model):
    # 学校名称
    schoolName = models.CharField(max_length=200)
    # 学校地址
    schoolAddress = models.CharField(max_length=200)
    # 学校类型
    schoolType = models.CharField(max_length=200)
    # 学校描述
    schoolDescription = models.TextField()
