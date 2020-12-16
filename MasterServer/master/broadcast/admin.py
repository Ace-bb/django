from django.contrib import admin

# Register your models here.

from .models import BroadcastRoom,roomEvaluate
# Register your models here.
admin.site.register(BroadcastRoom)
admin.site.register(roomEvaluate)