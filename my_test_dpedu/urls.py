"""my_test_dpedu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# URL的变量类型有字符类型，整型，slug和uuid，字符类型和整型为最常用类型
# 字符类型：匹配任何非空字符串，但不含斜杠。如果没有指定类型，默认使用该类型。
# 整型：匹配0和正整数。
# slug:可理解为注释，后缀或附属等概念，常作为URL的解释性字符。可匹配任何ASCII字符及连接符和下划线，能屎URL更加清晰易懂。
# uuid:匹配一个uuid格式的对象。为防止冲突，规定必须使用破折号并且所有字母必须小写，如075194d3-6885-417e-a8a8-6c931e272f00

# 在编写URL规则时，如果需要设置额外参数，规则如下：
# 参数只能以字典形式表示。
# 设置的参数只能在视图函数中读取和使用。
# 字典的一个键值对代表一个参数，键代表参数名，值代表参数值。
# 参数值没有数据格式限制，可以为某个对象，字符串或列表（元组）等。

# 根目录的urls.py导入admin功能模块
from django.contrib import admin
# 导入URL编写模块
from django.urls import path,include
from django.conf.urls import include, url
from index import views
from .  import views

# 列表包含了项目中的应用程序的URL，path的代码包含模块admin.site.urls，该模块定义了可在admin管理网站中请求的所有URL
# 整个项目的URL集合，每个元素代表一条URL信息
urlpatterns = [
    # 后台主页，admin/代表浏览器访问地址：localhost:8000/admin/
    # admin.site.urls是URL的处理函数，也称视图函数。
    path('admin/', admin.site.urls),
    # 主页，path的URL为空，代表网站的域名，及127.0.0.1:8000，通常是网站的首页，include将该URL分发给index的urls.py处理
    # 注销掉下面这行则显示index.html
    path('', include('index.urls')),
    path('', views.index),
    # 输入数据库手机id参数+.html访问相应页面
    path('<int:id>.html', views.model_index),

    # path(r'', include('my_test_dpedu.ruls', namespace='my_test_dpedu')),
    # path(r'^$', views.index(), name='index')

]
