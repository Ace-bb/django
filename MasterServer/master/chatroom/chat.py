from django.http import JsonResponse
from student.models import student, HadSendMessage
from chatroom.models import ChatRoom, ChatRecord, ChatHistroy
import json
from django.shortcuts import render


def chatHtml(request):
    students = list(student.objects.values().filter(accountId='10001'))
    # print(students)
    chatRecords = list(ChatRecord.objects.values())
    # print("chatRecords: ", chatRecords)
    chatHistory = list(ChatHistroy.objects.values())
    # print("chatHistory", chatHistory)
    if len(chatHistory) > 10:
        chatHistory = chatRecords[0:10]
    return render(request, 'message.html',
                  {'students': students[0], 'chatRecords': chatRecords, 'chatHistory': chatHistory})


def sendMessage(request):
    sendName = request.POST.get('userID', None)
    receiveName = request.POST.get('receiveName', None)
    message = request.POST.get('message', None)
    record = ChatRecord.objects.create(recordId='10001',
                                       sendName=sendName,
                                       sendTime = '2020-8-20',
                                       receiveName=receiveName,
                                       message=message)
    print("record: ", record)
    return JsonResponse({'ret': 0})
