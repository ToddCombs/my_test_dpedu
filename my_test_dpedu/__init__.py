from django.apps import AppConfig
import os

# 修改APP在Admin后台显示的名称，default_app_config的值来自于apps.py的类名
default_app_config = 'my_test_dpedu.AdminConfig'

def get_current_app_name(_file):
    """获取当前app的命名"""
    return os.path.split(os.path.dirname(_file))[-1]

class AdminConfig(AppConfig):
    """重写IndexConfig类"""
    name = get_current_app_name(__file__)
    # 设置项目在admin后台显示的名称
    verbose_name = '大鹏教育admin后台'