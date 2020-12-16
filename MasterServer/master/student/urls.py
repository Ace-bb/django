from django.urls import path

from . import views, classmanage

urlpatterns = [
    path('bs', views.sendMesHtml),
    path('send', views.sendMes),
    path('classmanage', classmanage.backHtml),
]