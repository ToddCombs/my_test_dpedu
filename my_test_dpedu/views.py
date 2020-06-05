# author:ToddCombs
from django.shortcuts import render
from django.http import HttpResponse
from index.form import *

def index(request):
    """my_test_dpedu主页"""
    return HttpResponse(request, 'data_form.html')

def model_index(request, id):
    """表单与模型"""
    if request.method == 'GET':
        instance = Product.objects.filter(id=id)
        # 判断数据是否存在
        if instance:
            product = ProductModelForm(instance=instance[0])
        else:
            product = ProductModelForm()
        return render(request, 'data_form.html', locals())
    else:
        product = ProductModelForm(request.POST)
        if product.is_valid():
            # 获取weight数据，并通过clean_weight进行清洗，转换成Python数据类型
            weight = product.cleaned_data['weight']
            product_db = product.save(commit=False)
            product_db.name = '我的Iphone'
            product_db.save()
            return HttpResponse('提交成功！weight清洗后的数据为： ' + weight)
        else:
            error_msg = product.errors.as_json()
            print(error_msg)
            return render(request, 'data_form.html', locals())

# def index(request):
#     """第二首页"""
#     # return render(request, 'index.html',context={'title': '首页'}, status=500)
