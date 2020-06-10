from django.contrib import admin
from .models import *
# Register your models here.
# 注册方法一，直接注册，显示数据库中所有条目：
# admin.site.register(Product)
admin.site.register(Type)

# 注册方法二（日常常用），自定义ProductAdmin类使其继承ModelAdmin。ModelAdmin主要是指模型信息如何展现在Admin后台系统中：
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """设置模型Product显示的字段"""
    list_display = ['id','name','weight','size','type']
    # 设置可搜索字段并在admin后台数据生成搜索框，如有外键应使用双下划线链接两个模型的字段
    search_fields = ['id','name','type__type_name']
    # 设置过滤器，在后台数据的右侧生成导航栏，如有外键，应使用双下划线链接两个模型的字段
    list_filter = ['name','type__type_name']
    # 设置排序方式，['id']是升序，['-id']是降序
    ordering = ['id']
    # 设置时间选择器，如字段中又时间格式才可以使用
    # date_hierarchy = Field
    # 在添加新数据时，设置克添加数据的字段
    fields = ['name','weight','size','type']
    # 设置可读字段，在修改或新增数据时使其无法设置
    readonly_fields = ['name']
    #在list_display里追加颜色类型
    list_display.append('colored_type')

    # 判断用户请求是否为超级用户，如果是，则重新设置readonly_fields属性（admin权限则可编辑产品名称）
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = []
        return self.readonly_fields

    # 重写当前用户名的访问权限，判断当前用户身份，超级用户则返回Product全部数据，否则只返回前5条
    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(id_lt=6)

    # 重写新增产品的下拉菜单，实现下拉框数据的过滤，admin用户新增产品下拉菜单显示全部选项，root用户显示部分
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'type':
            if not request.user.is_superuser:
                kwargs["queryset"] = Type.objects.filter(id__lt=4)
        return super(admin.ModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    # 重写新增或修改数据点击保存按钮触发的功能，该功能主要对输入的数据进行入库和更新处理
    def save_model(self, request, obj, form, change):
        if change:
            # 获取当前用户名
            user = request.user
            # 使用模型获取数据，pk代表具有主键属性的字段
            name = self.model.objects.get(pk=obj.pk).name
            # 使用表单获取数据
            weight = form.cleaned_datap['weight']
            # 写入日志
            f =open('C://MyDjango_log.txt', 'a')
            f.write('产品：'+str(name)+', 被用户：'+str(user)+'修改'+'\r\n')
            f.close()
        else:
            pass
        # 使用super克自定义save_model既保留父类已有的功能又添加自定义功能
        # 先判断change是否为True，如是，则说明当前操作为数据修改，反之为新增数据。
        super(ProductAdmin, self).save_model(request, obj, form, change)

    # 删除数据所执行的函数
    def delete_model(self, request, obj):
        pass
        super(ProductAdmin, self).delete_model(request, obj)


# @admin.register(Type)
# class TypeAdmin(admin.ModelAdmin):
#     """设置模型Type显示的字段"""
#     list_display = ['id','type_name']

# 修改admin站的项目title和header
# admin.site.site_title = 'My_test_dpedu后台管理'
# admin.site.site_header = 'My_test_dpedu'
#
