# author:ToddCombs
# 设置四个不同的URL地址，分别代表用户登陆，注册，修改密码和注销。
# 主要用来接收和处理根目录urls.py的请求信息
from django.urls import path
from . import views
urlpatterns = [
    path('login.html', views.loginView, name='login'),
    path('register.html', views.registerView, name='register'),
    path('setpassword.html', views.setpasswordView, name='setpassword'),
    path('logout.html', views.logoutView, name='logout'),
]