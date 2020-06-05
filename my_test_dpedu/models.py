# author:ToddCombs
# 每次修改models.py后，或者添加了一个新模型，都需要控制台执行命令python manage.py makemigrations my_test_dpedu
# 以及执行python manage.py migrate  。生成新的迁移文件，使其能够存储与模型Entry相关的信息。目的是告诉Django如何修改数据库

# 再django中，虚拟对象数据库也称为模型。通过模型实现对目标数据库的读写操作，实现方法如下：
# 1.配置目标数据库信息，主要在settings.py中设置数据库信息，参见《玩转django2.0》2.4节
# 2.构建虚拟对象数据库，在app的models.py文件中以类的形式定义模型。
# 3.通过模型在目标数据库中创建相应的数据表。
# 4.在视图函数中通过对模型操作实现目标数据库的读写操作。
# 一个模型对应目标数据库的一个数据表，每个数据表之间可以存在关联，表与表之间有三种关系：1对1，1对多，多对多。
# 一对一：a表的某一行数据只与b表的某一行数据相关，同时b表的某一行数据也只与a表的某一行数据相关。
# 一对多：a表的数据可以与b表的一到多行数据进行关联，但b表每一行数据只能与a表的某一行进行关联。
# 多对多：a表的某一行数据可以与b表的一到多行数据进行关联，同时在b表中的某一行数据也可与a表的一到多行数据进行关联。

# 查询条件get与filter差异：
# get查询字段必须是主键或者唯一约束的字段，且查询的数据必须存在，如果查询字段有重复或者不存在，则程序抛出异常信息。
# filter查询字段没有限制，只要该字段是数据表某一字段即可。查询结果以列表形式返回，如果查询结果为空，就返回空列表。

# 多表查询使用select_related方法：以index的Product，Type两个模型为例，设置select_related的参数值为“type”，该参数是Product定义的type字段
# 如果在查询过程中需要使用另一个表的字段，可使用“外键_字段名”来指向该表字段。
from django.db import models

class Topic(models.Model):
    """用户学习的主题类定义了两个属性text,date_added"""
    # text属性告诉Django该在数据库中预留多少空间(200个字符)。
    text = models.CharField(max_length=200)
    # 记录日期和时间的数据，传递实参True，每当创建新主题时，都会让Django自动设置成当前日期和时间。
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示，返回储存在属性text中的字符串"""
        return self.text

# 继承了Django基类Model
class Entry(models.Model):
    """学到的某个主题的具体知识"""
    # 外键引用了数据库中的另一条记录，这些代码将每个条目关联刀特定的主题，每个主题创建时，都给他分配了一个键或ID
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # Meta存储用于管理模型的额外信息。
    class Meta:
        verbose_name_plural = '条目'

    def __str__(self):
        """返回模型的字符串表示"""
        # text[:50]表示在admin管理站当中，只显示标题的开头部分而不是所有文本
        # “测试用文本——摘自百度百科 国际象棋（Chess），又称西洋棋，是一种二人对弈的棋类游戏。 棋盘...”后面用...表示
        return self.text[:50] + "..."

