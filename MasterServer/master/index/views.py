from django.shortcuts import render
from django.http import HttpResponse
from teacher.models import Teachers
import json

# Create your views here.
index = '''<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <title>搜索框demo</title>
 <style type="text/css">
  *{
   margin: 0;
   padding: 0;
  }
  body{
   width: 100vw;
   height: 100vh;
   background: radial-gradient(at center,
    #3498db,#2980b9);
   display: flex;
   justify-content: center;
   align-items: center;
  }
  div.search{
   height: 40px;
   width: 500px;  
  }
  div.search form{
   width: 100%;
   height: 100%;
  }
  div.search form input:nth-child(2){
   width: 400px;
   height: 100%;
   font-size: 16px;
   text-indent: 40px;
   border: none;
   float: left;
  }
  div.search form input:nth-child(3){
   width: 100px;
   height: 100%;
   font-size: 16px;
   letter-spacing: 5px;
   border: none;
  }
  div.search form img{
   position: absolute;
   left: 50vw;
   transform: translateX(-250px);
   margin-top: 10px;
   margin-left: 10px;
   height: 20px;
  }
 </style>
</head>
<body>
 <div class="search">
  <form action="http://127.0.0.1:8087/course/courses/" method="get">
   <img src="https://s3.ax1x.com/2020/12/03/D77yjJ.png" alt="">
   <input type="text" id="search" required name="condition" placeholder="请输入搜索条件">
   <input type="submit" value="搜索">
  </form> 
 </div>
</body>
</html>
'''


def listIndex(request):
    teachers = Teachers.objects.values()
    resList = list(teachers)
    introList = []
    for i in range(6):
        introList.append({"teacherName": resList[i]['teacherName'],
                          "icon": resList[i]['icon'],
                          "teacherPosition": resList[i]['teacherPosition'],
                          "schoolName": resList[i]['schoolName'],
                          "teacherIntro": resList[i]['brief_introduction']})
    print(introList)
    return render(request, 'about.html', {'introList': introList})
