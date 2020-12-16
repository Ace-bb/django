from django.db import models

# Create your models here.
class BroadcastRoom(models.Model):
    # 直播间id
    broadcastRoomId = models.CharField(max_length=100)
    # 直播间名
    roomName = models.CharField(max_length=200)
    # 主播导师名
    teacherName = models.CharField(max_length=100)
    # 导师ID
    teacherId = models.CharField(max_length=100)
    # 直播时间
    liveTime = models.DateTimeField()
    # 直播间主题内容
    broadcastTitle = models.CharField(max_length=200)

class roomEvaluate(models.Model):
    # 直播间ID
    broadcastRoomId = models.CharField(max_length=100)
    # 评价时间
    evaluateTime = models.DateTimeField()
    # 评论内容
    evaluateMessage = models.TextField()
    # 评价用户ID
    evaluateAccount = models.CharField(max_length=100)