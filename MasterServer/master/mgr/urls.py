from django.urls import path

from mgr import students, login_in_out

urlpatterns = [
    path('students', students.dispatcher),
    path('in', login_in_out.signin),
    path('out', login_in_out.signout),
]