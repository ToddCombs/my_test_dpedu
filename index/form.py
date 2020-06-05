# author:ToddCombs
# localhost:8000/data_form.html由form.py,views.py和data_form.html共同实现
# 在form.py中定义表单ProductForm，表单以类的形式表示。在表单中定义了不同类型的类属性，这些属性在表单中称为表单字段，每个表单字段代表HTML里的一个控件。
# 在views中导入form.py所定义的ProductForm类，在视图函数index_form中对ProductForm实例化生成对象product，再将对象product传递给模板data_form.html
# 模板data_form.html将对象product以HTML的<table>形式展现在网页上，记得最后需要在urls.py中添加path内容

# 表单的定义以为例： name = forms.CharField(max_length=20, label='名字',)
#                   name的参数label将转换成HTML的标签<label>
#                   字段name的forms.CharField类型转换成HTML的<input type="text">控件，标签<input>是一个输入框控件，
#                   type="text"代表当前输入框为文本输入框，参数type用于设置输入框的类型。
#                   字段name的命名转换成<input>控件的参数name,表单字段的参数max_length将转换成<input>的参数required maxlength

# 一个完整的表单主要有4个组成部分：提交地址，请求方式，元素控件和提交按钮。
# 提交地址用于设置用户提交的表单数据应由哪个URL接收和处理，由控件<form>的属性action决定。当用户向服务器提交数据时，若属性action为空，
# 提交的数据应由当前的URL来接收和处理，否则网页会跳转到属性action所指向的URL地址。
# 请求方式用于设置表单的提交方式，通常是GET请求或POST请求，由控件<form>的属性method决定。
# 元素控件是供用户输入数据信息的输入框，由HTML的<input>控件实现，其控件属性type用于设置输入框的类型，常用的输入框由文本框，下拉框和复选框等。
# 提交按钮供用户提交数据到服务器，该按钮也是由HTML的<input>控件实现。但该按钮具有一定的特殊性，因此不归纳到元素控件的范围内。

# django的表单功能主要是通过定义表单类，再由类的实例化生成HTML的表单元素控件，这样可以再模板中减少HTML的硬编码，每个HTML的表单元素控件由表单字段来决定。
# 数据表单是将模型的字段转换成表单的字段，再从表单的字段生成HTML的元素控件，这是日常开发中常用的表单之一
# 数据表但以类的形式定义，其内部可分为三大部分：添加模型外的表单字段，模型与表单设置和自定义函数。
# 添加模型外的表单字段是在模型已有字段下添加额外的表单字段。
# 模型与表单设置是将模型的字段转换成表单字段，由类Meta的属性实现两者的字段转换。
# 自定义函数是重写模块ModelForm中的函数，使其符合开发需求，如重写初始化函数__init__和自定义数据清洗函数等。

from django import forms
from .models import *
from django.core.exceptions import ValidationError


# 自定义数据验证函数
def weight_validate(value):
    """自定义表单，当用户输入异常时抛出提示信息，if not str(value).isdigit，判断用户输入不是数字的话就抛出异常提示信息"""
    if not str(value).isdigit():
        raise ValidationError('请输入正确的重量')


class ProductForm(forms.Form):
    """表单相关，设置错误信息并设置样式，如果用户输入为空格，则提示名字不能为空"""
    # name的参数label转换成HTML的标签<label>值，from.CharField类型转换成HTML的<input type="text">控件
    # 表单字段name的命名转换成<input>控件的参数name的值，name的参数max_length转换成<input>的参数required maxlength
    name = forms.CharField(max_length=20, label='名字',widget=forms.widgets.TextInput(attrs={'class':'cl'}),
                           error_messages={'required':'名字不能为空'},)
    # 使用自定义数据验证函数
    weight = forms.CharField(max_length=20, label='重量',validators=[weight_validate])
    size = forms.CharField(max_length=20, label='尺寸')
    # aa = forms.CharField(max_length=30,label='试试啊')
    choices_list = [(i+1,v.get('type_name')) for i,v in enumerate(Type.objects.values('type_name'))]
    # 设置css样式，类型必选
    type = forms.ChoiceField(widget=forms.widgets.Select(attrs={'class':'type','size':'4'}),choices=choices_list, label='产品类型')


class ProductModelForm(forms.ModelForm):
    """添加模型外的表单字段"""
    # 重写初始化函数
    def __init__(self, *args, **kwargs):
        super(ProductModelForm, self).__init__(*args, **kwargs)
        # 设置下拉框的数据
        # type_obj = Type.objects.values('type_name')
        # choices_list = [(i + 1, v['type_name']) for i, v in enumerate(type_obj)]
        # self.fields['type'].choices = choices_list
        # 初始化字段name，如果设置了值，在进入页面后文本框会有默认名称
        self.fields['name'].initial = ''
    productId = forms.CharField(max_length=20, label='产品序号')#,initial='NO1')
    # 模型与表单设置
    class Meta:
        """绑定模型"""
        model = Product
        fields = ['name', 'weight', 'size', 'type']
            # exclude用于禁止模型字段转换表单字段
        exclude = []
            # labels 设置HTML元素控件的label标签
        labels = {
            'name':'产品名称',
            'weight':'重量',
            'size':'尺寸',
            'type':'产品类型',
        }
            # 定义widgets,设置表单字段的css样式
        widgets = {
            'name':forms.widgets.TextInput(attrs={'class':'cl'}),
        }
            # 定义字段的类型，一般情况下模型字段会自动转换成表单字段
        field_classes = {
            'name':forms.CharField
        }
            # 帮助提示信息
        help_texts = {
            'name':'这是帮助'
        }
            # 自定义错误信息
        error_messages = {
                # __all__设置全部错误信息
            '__all__':{'required':'请输入内容',
                        'invalid':'请检查输入内容'},
                # 设置某个字段的错误信息
            'weight':{'required':'请输入重量数值',
                        'invalid':'请检查数值是否正确'}
        }

    def clean_weight(self):
        """自定表单字段weight的数据清洗,获取字段weight的值"""
        data = self.cleaned_data['weight']
        return data+'g'