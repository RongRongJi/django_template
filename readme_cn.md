#django快速开发模板

> 2019-10-22

## 项目介绍

本项目为django快速开发模板，内包含网页路由、请求处理、数据库操作、定时任务等模块，并提供了用户注册、登录、登出、发送邮件等的代码示例。<br>
* 项目结构：
    * project_template : django相关配置
    * TestModel : 项目主app
    * utils: 工具类

* 项目环境：
    python3 \ mysql
    安装项目依赖
    ```
    pip install -r requirements.txt
    ```
    中途若有安装失败，可以手动进行安装，版本不一定要保持一致<br>

****

## 功能介绍
###网页及路由
django项目中的html、css、js等文件存放在TestModel\templates中<br>
project_template中的urls.py用来表示视图的信息。<br>
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^hello$', views.index_webpage),
    url(r'^login$', views.alogin),
    url(r'^logout$', views.alogout),
    url(r'^register$', views.aregist)
]
```
TestModel中的views.py用来编写视图的具体内容，在示例中已提供了用户登录、登出、注册以及访问网页的相关代码<br>
运行django之后，通过访问http://127.0.0.1:8000/hello来访问hello.html，打开成功即为部署成功<br>

###请求处理
TestModel中的views.py可以用来编写服务器接口的详细内容<br>
```python
def alogin(request):
    if not request.method == 'POST':
        return HttpResponseNotAllowed(['POST',])
    if request.user.is_authenticated():
        return HttpResponse("{'status':'success'}")
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    user = authenticate(username=username,password=pwd)
    if user is not None:
        login(request, user)
        return HttpResponse(json.dumps({"status":"success"}),content_type="application/json")
    else:
        return HttpResponse(json.dumps({"status":"failed"}),content_type="application/json")
```
request.method可以用来限定POST、GET等方法<br>
函数的返回值为response，这里以json为例<br>

###数据库操作
本模板选择mysql作为数据库<br>
修改project_template中db.cfg配置文件，将数据库的配置改成自己的配置即可<br>

TestModel中的models.py用于编写数据库的表结构<br>
```python
class User_Template(models.Model):
    user = models.OneToOneField(User,on_delete=None)
    head_img = models.ImageField(upload_to='',default='',height_field='head_height',
                                 width_field='head_width')
    head_height = models.PositiveIntegerField(default=200)
    head_width = models.PositiveIntegerField(default=200)
    email = models.CharField
    conf = models.CharField(max_length=2300, null=False, default='{}')
```
编写好各种实体类的属性之后，输入以下命令可以将models.py中的实体类转换为数据库中的表结构<br>
```
python manage.py makemigrations
python manage.py migrate
```
登录数据库，`show tables`可以看到表已建好<br>

###定时任务
本模板中的定时任务使用Celery<br>
TestModel中的tasks.py用于编写各种定时任务，本模板提供发送邮件的定时任务作为实例<br>
在编写定时函数时必须在函数前标注@shared_task<br>
之后创建超级用户
```
python manage.py createsuperuser
```
创建完毕后，启动django服务器，在浏览器中访问127.0.0.1:8000/admin，用刚才创建的用户登录<br>
- 点击Periodic tasks可以添加已经编写好的定时任务
- 点击Crontabs \ Intervals可以设置定时任务的时间

###发送邮件
TestModel的tasks.py中已提供给发送邮件的示例<br>
在project_template的settings.py中，需要根据自己的邮箱对配置进行修改<br>
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_HOST = ''
EMAIL_PORT = 465
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = ''
```

****

|Author|RongRongJi|
|---|---
|Contact|[homepage](https://github.com/RongRongJi)