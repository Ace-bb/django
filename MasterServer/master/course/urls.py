from django.urls import path

from . import views, initPage

urlpatterns = [
    path('courses/', views.listorders),
    path('types/', initPage.dispatcher),
]