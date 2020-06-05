# author:ToddCombs
# 视图函数
# request:　用于生成响应的请求对象
# template_name:　要使用的模板的完整名称, 可选的参数
# context:　添加到模板上下文的一个字典. 默认是一个空字典. 如果字典中的某个值是可调用的, 视图将在渲染模板之前调用它.
# content_type:　 生成的文档要使用的MIME类型. 默认为DEFAULT_CONTENT_TYPE设置的值. 默认为"text/html"
# status:　响应的状态码. 默认为200
# using:　用于加载模板的模板引擎的名称
# render 结合一个给定的模板和一个给定的上下文字典, 并返回一个渲染后的HttpResponse对象。

# HttpResponse('Hello world') ——http状态码200，请求已成功被服务器接收
# HttpResponseRedirect('/admin/') ——http状态码302，重定向admin站点的URL
# HttpResponsePermanentRedirect('/admin/') ——http状态码301，永久重定向Admin站点的URL
# HttpResponseBadRequest('BadRequest') ——http状态码400，访问的页面不存在或者请求错误
# HttpResponseNotFound('NotFound') ——http状态码404，网页不存在或网页的URL失效
# HttpResponseForbidden('NotFound') ——http状态码403，没有访问权限
# HttpResponseNotAllowed('NotAllowedGet') ——http状态码405，不允许使用该请求方式
# HttpResponseServerError('ServerError') ——http状态码500，服务器内容错误
from django.http import HttpResponse
from django.shortcuts import render
import csv
from flask import redirect
from django.views.generic import ListView

# Create your views here.
from index.models import Product
from .form import ProductForm


def index(request):
    """Django2.0试做"""
    # type_list用于查询数据表字段type的数据并去重，
    type_list = Product.objects.values('type').distinct()
    # name_list用于查询数据表字段type和name的全部数据
    name_list = Product.objects.values('name','type')
    # 查询所得的数据以字典形式写入变量context种，变量context是render()函数的参数，作用是将变量传递给HTML模板。
    title = '首页'
    # context = {'title':'首页', 'type_list':type_list, 'name_list':name_list}
    # 当HTML模板接到变量type_list和name_list后，模板引擎解析模板语法并生成HTML文件
    # 小提示：变量context是以字典形式传递给HTML模板的，开发过程中如果传递变量果多使用context时就显得非常冗余，不利于维护更新
    # 因此使用locals()函数取代变量context，方法为在视图函数种所定义的变量名一定要与HTML模板的变量名相同才能生效
    # 如视图函数的type_list与HTML模板的type_list，两者的变量名一致才能将视图函数的变量传递给HTML模板
    return render(request, 'index.html',context=locals(), status=200)
    # return render(request, 'data_form.html'.locals())
    # 以下是返回状态码为500，且title已变更为首页
    # return render(request, 'index.html',context={'title':'首页'}, status=500)



def my_date(request, year, month, day):
    """年月日变量"""
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day))

# 用户访问该URL时，根据URL信息选择试图函数my_year处理，并将该URL命名为my_year
# 视图函数my_year将模板my_year.html作为响应内容并生成相应的网页返回给用户。
def my_year(request, year):
    """年参数name"""
    return render(request, 'my_year.html')


# 函数render()的request, 和template_name是必须的参数，其余参数是可选参数。
# request：浏览器向服务器发送的请求对象，包含用户信息，请求内容和请求方式等。
# template_name：html模板文件名，用户生成HTML网页
# context: 对html模板的变量赋值，以字典格式表示，默认情况下是一个空字典。
# content_type:响应数据的数据格式，一般情况下使用默认值即可。
# status:http状态码，默认为200
# using:设置HTML模板转换生成HTML网页的模板引擎
def my_year_dict(request, year, month):
    """参数为字典的URL的视图函数"""
    return render(request, 'my_year_dict.html', {'month':month})

def download(request):
    """http请求状态码"""
    # 当接受到用户请求后，视图函数download首先定义HttpResponse的相应类型文件为(text/csv)类型，生成response对象
    response = HttpResponse(content_type='text/csv')
    # 然后再response对象上定义Content-Disposition，设置浏览器下载文件的名称。attachment设置文件的下载方式，filename为文件名。
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    # 最后使用CSV模块加载response对象，把数据写入response对象所设置的CSV文件并将response对象返回到浏览器上，从而实现文件下载。
    writer = csv.writer(response)
    writer.writerow(['First row', 'A', 'B', 'C', 'This is a text file. Do not write Chinese.'])
    return response


# 如果想要将数据库的数据展现在网页上，需要由视图views，模型models，模板templates共同实现：
# 1，定义数据模型models，以类的方式定义数据表的字段。在数据库创建数据表时，数据表由模型定义的类生成。
# 2，在视图views导入模型所定义的类，该类也称为数据表对象，Django为数据表对象提供独有的数据操作方法，可实现数据库操作，从而获取数据表的数据。
# 3，视图函数获取数据后，将数据以字典，列表或对象的方式传递给HTML模板templates，并由模板引擎接收和解析，最后渲染成相应的HTML网页。

# request常用属性：
# COOKIES，获取客户端Cookies信息，data = request.COOKIES
# FILES，字典对象，包含所有上载文件。该字典有三个键：filename为上传文件的文件名；content-type为上传文件的类型；content为上传文件的原始内容，file = request.FILES
# GET，获取GET请求的请求参数，以字典形式存储，{'name':'TODD'}，request.GET.get('name')
# META，获取客户端的请求头信息，以字典形式存储，request.META.get('REMOTE_ADDR')获取客户端的IP地址
# POST，获取POST请求的请求参数，以字典形式存储，request.POST.get('name')，{'name':'TODD'}
# method，获取请求的请求方式（GET或POST请求），data = request.method
# path，获取当前请求的URL地址，path = request.path
# user，获取当前请求的用户信息，name = request.user.username，获取用户名

def login(request):
    """login请求方式，获取用户名"""
    # redirect()函数用于实现请求重定向，重定向链接以字符串形式表示。接受一个URL参数，表示让浏览器跳转去指定的URL.
    # return redirect('/')
    if request.method == 'POST':
        name = request.POST.get('name')
        # 绝对路径，完整的地址信息
        # return redirect('http://127.0.0.1:8000/')
    # 相对路径，代表首页地址
        return redirect('/')
    else:
        # 带参数请求地址http://localhost:8000/login.html?name=todd。返回username is todd
        if request.GET.get('name'):
            name = request.GET.get('name')
        # 不带参数请求地址http://localhost:8000/login.html。返回username is Everyone
        else:
            name = 'Everyone'
        return HttpResponse('username is ' + name)


# 通用视图三大类TemplateView，ListView，DetailView
# TemplateView模板视图直接返回HTML模板，但无法将数据库的数据展示出来
# ListView列表视图能将数据库的数据传递给HTML模板，通常获取某个表的所有数据。
# DetailView细节视图能将数据库的数据传递给HTML模板，通常获取数据表的单条数据。
class ProductList(ListView):
    """通用视图"""
    # context_object_name设置HTML模板的变量名称
    context_object_name = 'type_list'
    # 设定HTML模板
    template_name = 'index_view.html'
    # 查询数据
    queryset = Product.objects.values('type').distinct()

def get_context_data(self, **kwargs):
    """重写结果集方法，添加其他变量"""
    context = super().get_context_data(**kwargs)
    context['name_list'] = Product.objects.values('name','type')
    return context

def get_queryset(self):
    print(self.kwargs['id'])
    print(self.kwargs['name'])
    print(self.request.method)
    type_list = Product.objects.values('type').distinct()
    return type_list

def index_form(request):
    """提交表单相关"""
    # GET请求
    if request.method == 'GET':
        product = ProductForm()
        return render(request, 'data_form.html', locals())
    # POST请求
    else:
        product = ProductForm(request.POST)
        if product.is_valid():
        # 获取网页控件name的数据
            name = product['name']
            return HttpResponse('提交成功')
        else:
            error_msg = product.errors.as_json()
            print(error_msg)
            return render(request, 'data_form.html', locals())

