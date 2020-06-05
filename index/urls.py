# author:ToddCombs
# 在URL中引入正则表达式，首先导入re_path模块，正则表达式的作用是对URL的变量进行截取与判断，以小括号表示，

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    # 添加带有字符类型，整形和slug的url
    path('<year>/<int:month>/<slug:day>', views.my_date),
    # <year>年的格式为4位数字，输入3位或5位都会404，<month>,<day>均是如此
    # <year>前面的test/或者dict/为访问地址：http://localhost:8000/test/1111.html
    # 正则表达式末尾应加上斜杠或者其它字符，如果没有设置.html，则在浏览器上输入无限长的字符串，程序也能正常访问。
    # 每个小括号前后可使用斜杠或者其它字符将其分隔。例：<year>/<int:month>/<slug:day>
    # 每一个变量以一个小括号为单位，在小括号内，可分为三部分，以(?P<year>[0-9]{4})为例：
    # ?P是固定格式。<year>为变量的编写规则。[0-9]{4}是正则表达式的匹配模式，代表变量长度为4，只允许0-9的值
    re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html', views.my_date),
    # 设置参数name
    re_path('test/(?P<year>[0-9]{4}).html', views.my_year, name='my_year'),
    # 设置参数为字典的URL
    re_path('dict/(?P<year>[0-9]{4}).html', views.my_year_dict, {'month':'05'}, name='my_year_dict'),
    # 实现django下载csv文件功能，地址http://localhost:8000/download.html
    path('download.html', views.download),
    # login获取用户名
    path('login.html', views.login),
    # 通用视图ListView
    path('index/', views.ProductList.as_view()),
    # 表单相关
    path('data_form.html', views.index_form),



]