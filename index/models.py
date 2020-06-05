from django.db import models
from django.utils.html import format_html
# Create your models here.
# 以上内容将Product类和数据不Product构成映射关系，代码只是搭建两者的关系，在数据库中并没有生成相应的数据表。
# 我们可以再CMD窗口中使用python manage.py XXX命令通过Product类创建数据不Product
# 如果想要将index项目的模型展示在admin后台系统中，则需要在index的admin.py中添加代码注册
# python manage.py shell
# 数据查询是数据库操作中最复杂且内容最多的部分：from index.models import *    等同于SQL语句Select * from index_product
# 查询前5条数据，等同SQL语句：Select * from index_product LIMIT 5,数据以列表形式返回。p = Product.objects.all()[:5]
# 查询某字段，等同SQL语句：Select name from index_product,数据以列表形式返回，列表元素以字典格式表示 p = Product.objects.values('name')
# p = Product.objects.filter(id__gt=9)   查询id大于9的数据

class Type(models.Model):
    """创建产品分类表"""
    id = models.AutoField('序号', primary_key=True)
    type_name = models.CharField('类型名称', max_length=20)
    # 设置返回值，若不设置，则默认返回Type对象
    def __str__(self):
        return self.type_name

class Product(models.Model):
    """数据可视化"""
    # id = models.IntegerField(primary_key=True)
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('名称', max_length=50)
    # type = models.CharField(max_length=20)
    weight = models.CharField('重量', max_length=20)
    size = models.CharField('尺寸', max_length=20)
    # aa = models.CharField(max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='产品类型')
    # 设置返回值
    def __str__(self):
        return self.name

    class Meta:
        """如果只设置verbose_name，在Admin会显示为‘产品信息 s’"""
        verbose_name = '产品信息'
        verbose_name_plural = '产品信息'

    # 自定义函数，设置字体颜色
    def colored_type(self):
        if '手机' in self.type.type_name:
            color_code = 'red'
        elif '平板电脑' in self.type.type_name:
            color_code = 'blue'
        elif '智能穿戴' in self.type.type_name:
            color_code = 'green'
        else:
            color_code = 'yellow'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            self.type,
        )
    # 设置Admin的标题
    colored_type.short_description = '带颜色的产品类型'







