from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout


# 登录处理
def signin(request):
    # 从 HTTP POST 请求中获取用户名、密码参数
    userName = request.POST.get('username')
    passWord = request.POST.get('password')
    print(request.POST['username'])
    print("username:", userName)
    print("password:", passWord)
    # 使用 Django auth 库里面的 方法校验用户名、密码
    user = authenticate(username=userName, password=passWord)

    # 如果能找到用户，并且密码正确
    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login(request, user)
                # 在session中存入用户类型
                request.session['username'] = userName
                print("request.session:", request.session)
                status = request.session.get('usertype')
                print("request.session:", request.session)
                print("status:", status)
                if not status:
                    request.session['usertype'] = 'mgr'
                print("1:", userName)
                return JsonResponse({'ret': 0})
            else:
                return JsonResponse({'ret': 1, 'msg': '请使用管理员账户登录'})
        else:
            return JsonResponse({'ret': 0, 'msg': '用户已经被禁用'})

    # 否则就是用户名、密码有误
    else:
        return JsonResponse({'ret': 1, 'msg': '用户名或者密码错误'})


# 登出处理
def signout(request):
    # 使用登出方法
    logout(request)
    return JsonResponse({'ret': 0})