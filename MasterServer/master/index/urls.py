from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index.html', views.listIndex),
    path('about.html', views.listIndex),

] + static("/", document_root="./static")