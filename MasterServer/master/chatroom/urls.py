from django.urls import path

from . import views, chat

urlpatterns = [
    path('message.html', chat.chatHtml),
    path('sendmsg', chat.sendMessage),
]