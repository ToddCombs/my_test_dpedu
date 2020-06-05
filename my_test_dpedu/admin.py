# author:ToddCombs
# admin.py是向管理网站注册模型。
# 站点管理是整个网站APP管理界面，管理django的APP下所定义的模型.
# 认证和授权是django内置的认证系统，也是项目的一个app
# 用户和组是认证和授权所定义的模型，分别对应数据表auth_user和auth_user_groups。


from django.contrib import admin
from my_test_dpedu.models import Topic, Entry

# admin.site.register(Topic)
# admin.site.register(Entry)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """设置显示的字段"""
    list_display = ['id', 'text', 'date_added']

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    """设置显示的字段"""
    list_display = ['id', 'topic', 'text', 'date_added']