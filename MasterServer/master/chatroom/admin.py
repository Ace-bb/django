from django.contrib import admin

# Register your models here.
from .models import ChatRoom, ChatRecord, ChatHistroy

# Register your models here.
admin.site.register(ChatRoom)
admin.site.register(ChatRecord)
admin.site.register(ChatHistroy)
