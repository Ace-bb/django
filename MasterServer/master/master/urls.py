"""master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# 静态文件服务
from django.conf.urls.static import static
# 别忘了导入 listorders 函数
from course.views import listorders


urlpatterns = [
    path('admin/', admin.site.urls),

    # 凡是 url 以 sales/  开头的，
    # 都根据 sales.urls 里面的 子路由表进行路由
    path('course/', include('course.urls')),
    path('index/', include('index.urls')),
    path('api/mgr/', include('mgr.urls')),
    path('teacher/', include('teacher.urls')),
    path('login/', include('mgr.urls')),
    path('student/', include('student.urls')),
    path('chatroom/', include('chatroom.urls')),
] + static("/", document_root="./static")
